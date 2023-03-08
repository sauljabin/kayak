from rich.table import Table

from kayak.ksql.models import Server
from kayak.styles.colors import SECONDARY


class ServerInfo:
    def __init__(self, server: Server) -> None:
        self.server = server

    def __str__(self) -> str:
        return str(self.server)

    def __rich__(self) -> Table:
        table = Table(box=None, expand=False)
        table.add_column(style=f"{SECONDARY} bold")
        table.add_column()

        table.add_row("SERVER:", self.server.server)
        table.add_row("ID:", self.server.id)
        table.add_row(
            "VERSION:", self.server.version if self.server.version else "unknown"
        )
        table.add_row("STATUS:", self.server.status.lower())
        table.add_row("SERVICE ID:", self.server.service_id)

        return table
