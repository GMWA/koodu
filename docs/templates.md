# Available Templates

When installed, koodu also contains a series of templates that can be used to generate code for web applications based on a number of well-known frameworks.

## FastApi Template

With our FastApi template users are able to generate projects with the following structure:

```sh
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

* `models.py`: contains de definition of our models.
* `manage.py`: This is a cli tool to manage database migration in app.
* The `routers`: folder contains differents python file(one for each resource) and each file contains the differents endpoint(CRUD) implementation for the ressource.
* The `schemas`: folder contains differents python file(one for each resource) and each file contains the Schemas definitions for that ressource.
* `Dokerfile`: the Dockerfile manifest to build the app as docker image.

### The generated project use the following external paquets

* sqlalchemy
* pydantic


## Django Template

With our Django template users are able to generate projects with the following structure:

```sh
output/
├── project_name
│   ├── project_name_api/
│   │   ├── __init__.py
│   │   ├── migrations/
│   │   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── wsgi.py
├── manage.py
├── README.md
└── requirements.txt
```

* `config/`: directory is the actual Python package for your project.
* `manage.py`: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in [django-admin and manage.py](https://docs.djangoproject.com/en/4.2/intro/tutorial01/#:~:text=A%20command%2Dline%20utility%20that%20lets%20you%20interact%20with%20this%20Django%20project%20in%20various%20ways.%20You%20can%20read%20all%20the%20details%20about%20manage.py%20in%20django%2Dadmin%20and%20manage.py.).
* `project_name_api/migrations`: The directory that will contain project's migrations.
* `project_name_api/admin.py`: This will contain the administration for the app.
* `project_name_api/apps.py`: This content our app configurations.
* `project_name_api/models.py`: Our models are located in this file.
* `project_name_api/serializers.py`: This has the differents serializers (one for each model).
* `project_name_api/tests.py`: This will containts the tests for our api's endpoints.
* `project_name_api/urls.py`: This contains the urls definition od ours endpoints.
* `project_name_api/views.py`: This will contains ours views.


### The generated project use the following external paquets

* django
* django rest framework


## Flask Template

With our Flask template users are able to generate projects with the following structure:

```sh
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

* `models.py`: contains de definition of our models.
* `api`: folder contains differents folder(one for each resource) and each of these folders has:
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
