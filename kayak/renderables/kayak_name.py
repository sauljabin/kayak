from pyfiglet import Figlet
from rich.text import Text

from kayak import NAME, VERSION
from kayak.styles.colors import PRIMARY, SECONDARY


class KayakName:
    def __init__(self, include_version: bool = True):
        self.include_version = include_version

    def __str__(self) -> str:
        figlet = Figlet(font="chunky")
        text: str = figlet.renderText(NAME)
        return text.rstrip()

    def __rich__(self) -> Text:
        text = Text(str(self), style=f"{PRIMARY} bold")

        if self.include_version:
            text.append(f"v{VERSION}", style=f"{SECONDARY} bold")

        return text
