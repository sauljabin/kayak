from typing import Any, List
from urllib.parse import urljoin

import requests

from kayak.ksql.models import Server, Stream, Topic

KSQL_HEADERS = {"Accept": "application/vnd.ksql.v1+json"}
STATEMENT_PATH = "/ksql"
QUERY_PATH = "/query"

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
        response = requests.get(url, headers=KSQL_HEADERS)
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
        response = requests.post(url, json=data, headers=KSQL_HEADERS)
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
        response = requests.post(url, json=data, headers=KSQL_HEADERS)
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


if __name__ == "__main__":
    service = KsqlService("http://localhost:8088")
    print(service.info())
    print(service.streams())
    print(service.topics())
