import json


class Server:
    def __init__(
        self,
        id: str = "",
        server: str = "",
        service_id: str = "",
        status: str = "",
        version: str = "",
    ) -> None:
        self.id = id
        self.server = server
        self.service_id = service_id
        self.status = status
        self.version = version

    def __repr__(self) -> str:
        return json.dumps(
            {
                "id": self.id,
                "server": self.server,
                "service_id": self.service_id,
                "status": self.status,
                "version": self.version,
            }
        )

    def __str__(self) -> str:
        return str(self.server)
