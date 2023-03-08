from typing import Type

from textual.app import App, ComposeResult, CSSPathType
from textual.binding import Binding
from textual.driver import Driver
from textual.keys import Keys
from textual.widgets import Footer

from kayak.ksql.ksql_service import KsqlService
from kayak.styles.colors import DESIGN
from kayak.widgets.header import Header


class Tui(App[None]):
    CSS_PATH = "tui.css"
    BINDINGS = [
        Binding(Keys.ControlC, "quit", "QUIT"),
        Binding(Keys.F1, "push_screen('help')", "HELP"),
    ]

    def __init__(
        self,
        server: str,
        user: str | None,
        password: str | None,
        driver_class: Type[Driver] | None = None,
        css_path: CSSPathType | None = None,
        watch_css: bool = False,
    ):
        super().__init__(driver_class, css_path, watch_css)
        self.ksql_service = KsqlService(server, user, password)
        self.server = self.ksql_service.info()

    def on_mount(self) -> None:
        header = self.query_one(Header)
        header.server = self.server

        self.design = DESIGN
        self.refresh_css()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
