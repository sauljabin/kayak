import asyncio
import json
from typing import Any, Callable, Dict, List
from urllib.parse import urljoin

import httpx

from kayak.ksql.models import Server, Stream, Topic

TIMEOUT_1H = 60 * 60

KSQL_HEADERS = {"Accept": "application/vnd.ksql.v1+json"}
STATEMENT_PATH = "/ksql"
QUERY_PATH = "/query-stream"
INFO_PATH = "/info"


class KsqlService:
    def __init__(
        self,
        server: str,
        user: str | None = None,
        password: str | None = None,
    ):
        self.server = server
        self.user = user
        self.password = password

    def info(self) -> Server:
        url = urljoin(self.server, INFO_PATH)
        response = httpx.get(url, headers=KSQL_HEADERS)
        response.raise_for_status()

        def json_to_server(obj: dict[Any, Any], server: str) -> Any:
            if "KsqlServerInfo" in obj:
                return obj["KsqlServerInfo"]
            if "version" in obj:
                return Server(
                    id=obj["kafkaClusterId"],
                    service_id=obj["ksqlServiceId"],
                    status=obj["serverStatus"],
                    version=obj["version"],
                    server=server,
                )
            return obj

        server_obj: Server = response.json(
            object_hook=lambda d: json_to_server(d, self.server)
        )
        return server_obj

    def streams(self) -> List[Stream]:
        url = urljoin(self.server, STATEMENT_PATH)
        data = {"ksql": "LIST STREAMS EXTENDED;"}
        response = httpx.post(url, json=data, headers=KSQL_HEADERS)
        response.raise_for_status()

        def json_to_stream(obj: dict[Any, Any]) -> Any:
            if "sourceDescriptions" in obj:
                return obj["sourceDescriptions"]
            if "type" in obj and obj["type"] == "STREAM":
                return Stream(
                    name=obj["name"],
                    topic=obj["topic"],
                    key_format=obj["keyFormat"],
                    value_format=obj["valueFormat"],
                )
            return obj

        stream_list: List[Stream] = response.json(object_hook=json_to_stream)[0]
        return stream_list

    def topics(self) -> List[Topic]:
        url = urljoin(self.server, STATEMENT_PATH)
        data = {"ksql": "LIST TOPICS;"}
        response = httpx.post(url, json=data, headers=KSQL_HEADERS)
        response.raise_for_status()

        def json_to_topic(obj: dict[Any, Any]) -> Any:
            if "topics" in obj:
                return obj["topics"]
            if "name" in obj:
                return Topic(
                    name=obj["name"],
                )
            return obj

        topic_list: List[Topic] = response.json(object_hook=json_to_topic)[0]
        return topic_list

    async def query(
        self,
        query: str,
        earliest: bool = False,
        on_header: Callable[[dict[str, str]], None] = lambda columns: None,
        on_new_row: Callable[[list[Any]], None] = lambda row: None,
        on_close: Callable[[], None] = lambda: None,
    ) -> None:
        url = urljoin(self.server, QUERY_PATH)
        data = {
            "sql": query,
            "properties": {"ksql.streams.auto.offset.reset": "earliest"}
            if earliest
            else {},
        }

        async with httpx.AsyncClient(http2=True, timeout=TIMEOUT_1H) as client:
            async with client.stream(method="POST", url=url, json=data) as stream:
                async for chunk in stream.aiter_text():
                    if chunk:
                        results = json.loads(chunk)
                        if isinstance(results, Dict):
                            on_header(results)
                        elif isinstance(results, List):
                            on_new_row(results)

        on_close()


if __name__ == "__main__":
    service = KsqlService("http://localhost:8088")
    print(service.info())
    print(service.streams())
    print(service.topics())
    print("--QUERY--")
    # asyncio.run(service.push_query("SELECT * FROM orders EMIT CHANGES;", True))
    asyncio.run(
        service.query(
            "SELECT * FROM orders;",
            True,
            on_header=print,
            on_new_row=print,
            on_close=lambda: print("finished"),
        )
    )
    asyncio.run(
        service.query(
            "SELECT * FROM orderSizes;",
            True,
            on_header=print,
            on_new_row=print,
            on_close=lambda: print("finished"),
        )
    )
