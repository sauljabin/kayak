import click
import toml
from rich.console import Console

from scripts import CommandProcessor


@click.command()
@click.argument(
    "rule",
    nargs=1,
    type=click.Choice(["major", "minor", "patch"], case_sensitive=False),
)
def main(rule):
    """
    \b
    Examples:
        poetry run python -m scripts.bump major
        poetry run python -m scripts.bump minor
        poetry run python -m scripts.bump patch

    More info at https://python-poetry.org/docs/cli/#version and https://semver.org/.
    """

    init_commands = {
        "checking pending changes": "git diff --exit-code",
        "checking pending changes in stage": "git diff --staged --exit-code",
        "checking not pushed commits": "git diff --exit-code main origin/main",
        f"bumping to a [purple bold]{rule}[/] version": f"poetry version {rule}",
        f"bumping changelog to a [purple bold]{rule}[/] version": f"poetry run changelog release --{rule} --yes",
    }
    command_processor = CommandProcessor(init_commands)
    command_processor.run()

    toml_data = toml.load("pyproject.toml")
    new_version = toml_data["tool"]["poetry"]["version"]

    console = Console()

    confirmation = console.input(
        f"Release a new [purple bold]{rule}[/] version [bold purple]{new_version}[/] "
        f"([bold green]yes[/]/[bold red]no[/])? "
    )

    if confirmation != "yes":
        revert_commands = {
            "deleting changes": "git checkout .",
        }
        command_processor = CommandProcessor(revert_commands)
        command_processor.run()
        return

    confirm_commands = {
        "adding new version": "git add --all",
        "committing new version": f"git commit -m 'bumping version to {new_version}'",
        "adding new version tag": f"git tag v{new_version}",
        "pushing new changes": "git push origin main",
        "pushing tag": "git push --tags",
    }
    command_processor = CommandProcessor(confirm_commands)
    command_processor.run()


if __name__ == '__main__':
    main()
