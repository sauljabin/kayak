<p align="center">
<a href="https://github.com/sauljabin/kayak"><img alt="kayak" src="https://raw.githubusercontent.com/sauljabin/kayak/main/screenshots/banner.png"></a>
</p>


<a href="https://github.com"><img alt="GitHub" width="60" height="20" src="https://img.shields.io/badge/-github-blueviolet?logo=github&logoColor=white"></a>
<a href="https://github.com/sauljabin/kayak/blob/main/LICENSE"><img alt="MIT License" src="https://img.shields.io/github/license/sauljabin/kayak"></a>
<a href="https://github.com/sauljabin/kayak/actions"><img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/sauljabin/kayak/main.yml?branch=main"></a>
<br>
<a href="https://www.python.org/"><img alt="Python" width="60" height="20" src="https://img.shields.io/badge/-python-brightgreen?logo=python&logoColor=white"></a>
<a href="https://pypi.org/project/kayak"><img alt="Version" src="https://img.shields.io/pypi/v/kayak"></a>
<a href="https://pypi.org/project/kayak"><img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/kayak"></a>
<a href="https://pypi.org/project/kayak"><img alt="Platform" src="https://img.shields.io/badge/platform-linux%20%7C%20osx-0da5e0"></a>
<br>
<a href="https://ksqldb.io/"><img alt="ksqlDB" width="60" height="20" src="https://img.shields.io/badge/-ksqlDB-F05662?logo=apache-kafka&logoColor=white"></a>
<a href="https://pypi.org/project/ksql/"><img alt="ksqlDB Client" src="https://img.shields.io/pypi/v/ksql?label=client">
<a href="https://ksqldb.io/"><img alt="ksqlDB" src="https://img.shields.io/badge/version-0.28.3-blue"></a>
<br>
<a href="https://www.docker.com/"><img alt="Docker" width="60" height="20" src="https://img.shields.io/badge/-docker-blue?logo=docker&logoColor=white"></a>
<a href="https://hub.docker.com/r/sauljabin/kayak"><img alt="Docker Image Version (latest by date)" src="https://img.shields.io/docker/v/sauljabin/kayak?label=tag"></a>
<a href="https://hub.docker.com/r/sauljabin/kayak"><img alt="Docker Image Size (latest by date)" src="https://img.shields.io/docker/image-size/sauljabin/kayak"></a>

**kayak** is a [ksqlDB](https://ksqldb.io/) TUI (text user interface).

:rocket: This project is powered by [textual](https://github.com/willmcgugan/textual)
and [rich](https://github.com/willmcgugan/rich)!.

# Table of Contents

* [Table of Contents](#table-of-contents)
* [Installation and Usage](#installation-and-usage)
    * [Running with Docker](#running-with-docker)
* [Development](#development)
    * [Scripts](#scripts)
    * [Kafka Cluster](#kafka-cluster)
    * [Docker](#docker)
    * [Bumping Version](#bumping-version)

# Installation and Usage

Install with pip:

```shell
pip install kayak
```

> `pip` will install `kayak` and `kyk` aliases.

Upgrade with pip:

```shell
pip install --upgrade kayak
```

Help:

```shell
kayak --help
```

Version:

```shell
kayak --version
```

Run:

```shell
kayak http://ksqldb:8088
```

Run authenticated:

```shell
kayak --user user --password password http://ksqldb:8088
```

Run authenticated with input:

```shell
kayak http://ksqldb:8088 --user user --password
```

or

```shell
kayak --user user --password -- http://ksqldb:8088
```

> `kayak` will wait until you enter the password.

### Running with Docker

Using docker:

```shell
docker run --rm -it --network cluster sauljabin/kayak:latest http://ksqldb:8088
```

Aliases:

```shell
alias kayak='docker run --rm -it --network cluster sauljabin/kayak:latest'
alias kyk=kayak
```

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
poetry run kayak --help
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

### Kafka Cluster

Run local cluster:

```shell
cd cluster
docker compose up -d
```

> Open <http://localhost:8080/>

Run ksqlDB cli:

```shell
ksql http://localhost:8088
```

Import example:

```shell
ksql -f ksql/create-orders.ksql http://localhost:8088
ksql -f ksql/insert-orders.ksql http://localhost:8088
ksql -e "PRINT 'ksqldb.order_sizes' FROM BEGINNING;" http://localhost:8088
```

### Docker

Build docker image:

```shell
poetry run python -m scripts.docker
```

> Image tagged as `sauljabin/kayak:latest`.

Run with docker:

```shell
docker run --rm -it --network cluster sauljabin/kayak:latest http://ksqldb:8088
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

# TODO

- LIST QUERIES, CONNECTORS
- INPUT FOR QUERY
- STATEMENTS
- SETTINGS MENU (earliest, latest)
- ERROR MESSAGE