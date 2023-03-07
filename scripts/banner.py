from rich import box
from rich.console import Console
from rich.panel import Panel

from kayak.renderables.kayak_name import KayakName
from kayak.styles.colors import MAIN_COLOR


def main():
    console = Console()
    panel = Panel.fit(KayakName(False), box=box.ROUNDED, border_style=MAIN_COLOR)
    console.print(panel)


if __name__ == "__main__":
    main()
