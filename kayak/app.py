import os

import click
from rich.console import Console

from kayak.renderables.kayak_name import KayakName


@click.command()
@click.option("--version", is_flag=True, help="Show the app version and exit.")
@click.option(
    "--password",
    prompt=True,
    hide_input=True,
    prompt_required=False,
    default=lambda: os.environ.get("KSQLDB_PASSWORD", None),
    help="If your KSQL server is configured for authentication, then provide your password here. The username must be "
    "specified separately with the --user option. Use KSQLDB_PASSWORD env variable to set a default value.",
)
@click.option(
    "--user",
    default=lambda: os.environ.get("KSQLDB_USER", None),
    help="If your KSQL server is configured for authentication, then provide your user name here. The password must "
    "be specified separately with the --password option. Use KSQLDB_USER env variable to set a default value.",
)
@click.argument("server", nargs=1, required=False, default=None)
def main(
    version: bool, password: str | None, user: str | None, server: str | None
) -> None:
    """
    kayak is a ksqlDB TUI (text user interface).

    \b
    SERVER  The address of the Ksql server to connect to
            (ex: http://localhost:8088).
            This option may occur a maximum of 1 times.
    """

    console = Console()

    if version:
        console.print(KayakName())
        exit(0)

    if [user, password].count(None) == 1:
        console.print("[bold red]Please provide an --user and --password[/]")
        exit(1)

    if server is None:
        console.print("[bold red]Missing argument 'SERVER'[/]")
        exit(1)

    click.echo(f"{server} {user} {password}")


if __name__ == "__main__":
    main()
