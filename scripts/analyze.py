from scripts import CommandProcessor


def main():
    commands = {
        "checking types": "poetry run mypy kayak/",
        "checking imports": "poetry run isort --check .",
        "checking styles": "poetry run black --check .",
        "checking code standards": "poetry run flake8 .",
    }
    command_processor = CommandProcessor(commands)
    command_processor.run()


if __name__ == "__main__":
    main()
