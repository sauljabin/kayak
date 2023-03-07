from rich.columns import Columns
from rich.console import RenderableType
from textual.widgets import Static

from kayak.ksql.models import Server
from kayak.renderables.kayak_name import KayakName
from kayak.renderables.ksql_info import KsqlInfo


class Header(Static):
    server = Server()

    def render(self) -> RenderableType:
        kayak_name = KayakName()
        ksql_info = KsqlInfo(self.server)
        return Columns([kayak_name, ksql_info], padding=3)
