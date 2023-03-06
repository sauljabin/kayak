from scripts import CommandProcessor


def main():
    commands = {
        "removing old packages": "rm -rf dist",
        "building the project": "poetry build",
        "creating docker image": "docker build -t sauljabin/kayak:latest -f docker/Dockerfile .",
    }
    command_processor = CommandProcessor(commands)
    command_processor.run()


if __name__ == "__main__":
    main()
