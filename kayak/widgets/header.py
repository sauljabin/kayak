from rich.columns import Columns
from rich.console import RenderableType
from textual.widgets import Static

from kayak.renderables.kayak_name import KayakName


class Header(Static):
    def render(self) -> RenderableType:
        kayak_name = KayakName()
        return Columns([kayak_name], padding=3)
