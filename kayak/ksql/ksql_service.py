from urllib.parse import urljoin

import requests

from kayak.ksql.mappers import json_to_server
from kayak.ksql.models import Server

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

    def ksql_info(self) -> Server:
        url = urljoin(self.server, INFO_PATH)
        server: Server = requests.get(url).json(
            object_hook=lambda d: json_to_server(d, self.server)
        )
        return server


if __name__ == "__main__":
    service = KsqlService("http://localhost:8088")
    print(type(service.ksql_info()))
    print(repr(service.ksql_info()))
    print(str(service.ksql_info()))
