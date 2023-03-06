from rich import box
from rich.console import Console
from rich.panel import Panel

from kayak.renderables.kayak_version import KayakVersion
from kayak.styles.colors import ORANGE


def main():
    console = Console()
    panel = Panel.fit(KayakVersion(False), box=box.ROUNDED, border_style=ORANGE)
    console.print(panel)


if __name__ == "__main__":
    main()
