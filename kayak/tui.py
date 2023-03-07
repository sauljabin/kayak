from typing import Type

from textual.app import App, ComposeResult, CSSPathType
from textual.binding import Binding
from textual.driver import Driver
from textual.keys import Keys
from textual.widgets import Footer


class Tui(App[None]):
    CSS_PATH = "tui.css"
    BINDINGS = [
        Binding(Keys.ControlC, "quit", "QUIT"),
        Binding(Keys.F1, "push_screen('help')", "HELP"),
    ]

    def __init__(
        self,
        server: str | None,
        user: str | None,
        password: str | None,
        driver_class: Type[Driver] | None = None,
        css_path: CSSPathType | None = None,
        watch_css: bool = False,
    ):
        super().__init__(driver_class, css_path, watch_css)

    def compose(self) -> ComposeResult:
        yield Footer()
