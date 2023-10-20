# Available Templates

When installed, koodu also contains a series of templates that can be used to generate code for web applications based on a number of well-known frameworks.

## FastApi Template

With our FastApi template users are able to generate projects with the following structure:

```
output/
├── project_name
│   ├── __init__.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── *.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── *.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
├── Dockerfile
├── Makefile
├── manage.py
├── README.md
└── requirements.txt
```

* `models.py` contains de definition of our models.
* `manage.py`: This is a cli tool to manage database migration in app.
* The `routers` folder contains differents python file(one for each resource) and each file contains the differents endpoint(CRUD) implementation for the ressource.
* The `schemas` folder contains differents python file(one for each resource) and each file contains the Schemas definitions for that ressource.
* `Dokerfile`: the Dockerfile manifest to build the app as docker image.

### The generated project use the following external paquets

* sqlalchemy
* pydantic


## Django Template

With our Django template users are able to generate projects with the following structure:

```

```

## Flask Template

With our Flask template users are able to generate projects with the following structure:

```
output/
├── project_name/
│   ├── __init__.py
│   ├── api/
│   │   ├──__init__.py
│   │   ├──ressouce/
│   │   │   ├── controllers.py
│   │   │   ├── fields.py
│   │   │   ├── parsers.py
│   ├── models.py
├── manage.py
├── README.md
└── requirements.txt
```

* `models.py` contains de definition of our models.
* The `api` folder contains differents folder(one for each resource) and each of these folders has:
    * `controllers.py`: The controllers for the resource.
    * `fields.py`: The fields for the ressource.
    * `parsers.py`: The parsers for the resource.
* `api/__init__.py`: This is where the api is initialized as Blueprint.
* `__init__.py`: the is where the Flask app itself is initialized.
* `manage.py`: This is a cli tool to manage database migration in app.
* `Dokerfile`: the Dockerfile manifest to build the app as docker image.

### The generated project use the following external paquets

* Flask-SqlAlchemy
* Flask-Bcrypt
* Flask-Migrate
* Flask-RESTful
* Flask-Cors
* Flask-JWT-Extended


## Express.Js Template

With our Express template users are able to generate projects with the following structure:

```

```
