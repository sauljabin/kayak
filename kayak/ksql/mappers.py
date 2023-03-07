from typing import Any

from kayak.ksql.models import Server


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
