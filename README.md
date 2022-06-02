# Simple fastapi service with lambda

## Local development
In order to run locally you need the following:

- Python 3.7+
- A python virtual environment (conda or virtualenv)
- Docker
- docker-compose

### 1. Install requirements

```shell
$ pip install -r requirements.txt
$ pip install -r requirements-dev.txt
```

### 2. Run DynamoDB emulator

```shell
$ docker-compose up
```

### 3. Run service

```shell
$ python -m app.main
```

### 4. Run tests

```shell
$ pytest app
```

### 5. Formatting and linting

```shell
$ black app
$ pylint app
```

## Deploy Pipeline IaC

Refer to [docs](cloudformation/README.md)