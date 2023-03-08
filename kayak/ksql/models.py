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
        return repr(self)


class Stream:
    def __init__(
        self,
        name: str = "",
        topic: str = "",
        key_format: str = "",
        value_format: str = "",
    ) -> None:
        self.name = name
        self.topic = topic
        self.key_format = key_format
        self.value_format = value_format

    def __repr__(self) -> str:
        return json.dumps(
            {
                "name": self.name,
                "topic": self.topic,
                "key_format": self.key_format,
                "value_format": self.value_format,
            }
        )

    def __str__(self) -> str:
        return repr(self)


class Topic:
    def __init__(
        self,
        name: str = "",
    ) -> None:
        self.name = name

    def __repr__(self) -> str:
        return json.dumps({"name": self.name})

    def __str__(self) -> str:
        return repr(self)
