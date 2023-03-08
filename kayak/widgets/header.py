from rich.columns import Columns
from rich.console import RenderableType
from textual.widgets import Static

from kayak.ksql.models import Server
from kayak.renderables.kayak_name import KayakName
from kayak.renderables.server_info import ServerInfo


class Header(Static):
    server = Server()

    def render(self) -> RenderableType:
        kayak_name = KayakName()
        ksql_info = ServerInfo(self.server)
        return Columns([kayak_name, ksql_info], padding=3)
