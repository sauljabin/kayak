import asyncio
from typing import Any, Type

from textual.app import App, ComposeResult, CSSPathType
from textual.binding import Binding
from textual.containers import Container
from textual.driver import Driver
from textual.keys import Keys
from textual.widgets import DataTable, Footer, Input, Tree

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
        self.topics = self.ksql_service.topics()
        self.streams = self.ksql_service.streams()

    def on_mount(self) -> None:
        input_query = self.query_one(Input)
        input_query.placeholder = "QUERY"
        input_query.focus()

        header = self.query_one(Header)
        header.server = self.server

        tree = self.query_one(Tree)
        tree.show_root = False
        tree.root.expand()
        tree.cursor_line = -1

        stream_node = tree.root.add("STREAMS", expand=True)
        for stream in self.streams:
            stream_node.add_leaf(stream.name)

        topic_node = tree.root.add("TOPICS", expand=True)
        for topic in self.topics:
            topic_node.add_leaf(topic.name)

        table = self.query_one(DataTable)
        table.cursor_type = "row"

        self.design = DESIGN
        self.refresh_css()

    async def on_input_submitted(self, message: Input.Submitted) -> None:
        table = self.query_one(DataTable)
        table.focus()

        def on_header(columns: dict[str, str]) -> None:
            for column in columns["columnNames"]:
                table.add_column(column)

        def on_new_row(row: list[Any]) -> None:
            table.add_row(*row)
            table.scroll_end()

        asyncio.create_task(
            self.ksql_service.query(
                query=message.value, on_header=on_header, on_new_row=on_new_row
            )
        )

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

        yield Tree("")
        with Container():
            yield Input()
            yield DataTable()
