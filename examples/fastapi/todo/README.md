# Todo

## Project setup

### REQUIREMENTS

- python (3.x recommended) & pip (>= 22 recommended)
- docker
- make (a command line tool to run Makefile commands)

#### HOW TO SET UP

* Put appropriate parameters inside .env.example
* install dependencies

```sh
$ make install-deps
```

#### HOW TO LAUNCH

##### DEV

formating

```sh
$ make lint
```

##### PROD

Or Using Docker

* build your docker image

```sh
$ make docker-build
```

* run your project on port 8000

```sh
$ make docker-run
```

### To run the project [fastapi]

- Install the virtualenv

- Run the project

```sh
$ make run
```