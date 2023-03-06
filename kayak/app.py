import os
from typing import Any

import click
import validators
from click import Context, Parameter, ParamType
from rich.console import Console


class UrlType(ParamType):
    def convert(self, value: Any, param: Parameter | None, ctx: Context | None) -> Any:
        if not validators.url(str(value)):
            self.fail("It's not a valid url.", param, ctx)
        return value


@click.command()
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
@click.argument("server", nargs=1, type=UrlType())
def main(password: str | None, user: str | None, server: str) -> None:
    """
    kayak is a ksqlDB TUI (text user interface).

    \b
    SERVER  The address of the Ksql server to connect to
            (ex: http://localhost:8088).
            This option may occur a maximum of 1 times.
    """

    if [user, password].count(None) == 1:
        console = Console()
        console.print("[bold red]Please provide an user and password[/]")
        exit(-1)

    click.echo(f"{server} {user} {password}")


if __name__ == "__main__":
    main()
