from pyfiglet import Figlet
from rich.text import Text

from kayak import APP_NAME, APP_VERSION
from kayak.styles.colors import ORANGE


class KayakVersion:
    def __init__(self, include_version: bool = True):
        self.include_version = include_version

    def __str__(self) -> str:
        figlet = Figlet(font="chunky")
        figlet_string: str = figlet.renderText(APP_NAME).rstrip()
        return figlet_string

    def __rich__(self) -> Text:
        return Text.from_markup(
            f"[{ORANGE} bold]{self}[/]\n[green bold]v{APP_VERSION}[/]"
            if self.include_version
            else f"[{ORANGE} bold]{self}[/]"
        )
