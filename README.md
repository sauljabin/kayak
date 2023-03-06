<p align="center">
<a href="https://github.com/sauljabin/kayak"><img alt="kayak" src="https://raw.githubusercontent.com/sauljabin/kayak/main/screenshots/banner.png"></a>
</p>

# Development

Installing poetry:

```shell
pip install poetry
```

Installing development dependencies:

```shell
poetry install
```

Installing pre-commit hooks:

```shell
poetry run pre-commit install
```

Running kayak:

```shell
poetry run kayak
```

### Scripts

Running unit tests:

```shell
poetry run python -m scripts.tests
```

Applying code styles:

```shell
poetry run python -m scripts.styles
```

Running code analysis:

```shell
poetry run python -m scripts.analyze
```

Generate readme banner:

```shell
poetry run python -m scripts.banner
```

### Bumping Version

Help:

```shell
poetry run python -m scripts.release --help
```

> More info at https://python-poetry.org/docs/cli/#version and https://semver.org/.
> For changelog management check https://github.com/mc706/changelog-cli.

Upgrade (`major.minor.patch`):

```shell
poetry run python -m scripts.bump patch
```