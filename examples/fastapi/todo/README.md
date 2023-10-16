# Todo

## Project setup

### REQUIREMENTS

- python (3.x recommended) & pip (>= 22 recommended)
- docker
- make (a command line tool to run Makefile commands)

#### HOW TO SET UP

```
# Put appropriate parameters inside .env.example
make install-deps
```

#### HOW TO LAUNCH

##### DEV

# formating
make lint
```

##### PROD

Or Using Docker

```
# This will build your docker image
make docker-build
```

```
# This will install and run your project on port 8000
make docker-run
```

### To run the project [fastapi]

- Install the virtualenv

- Run the project
```
make run
```