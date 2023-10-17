# Available Templates

When installed, koodu also contains a series of templates that can be used to generate code for web applications based on a number of well-known frameworks.

## Flask Template

With our Flask template users are able to generate projects with the following structure:

```

```

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

* The `routers` folder contains differents python file(one for each resource) and each file contains the differents endpoint(CRUD) implementation for the ressource.

* The `schemas` folder contains differents python file(one for each resource) and each file contains the Schemas definitions for that ressource.

## Django Template

With our Django template users are able to generate projects with the following structure:

```

```

## Express.Js Template

With our Express template users are able to generate projects with the following structure:

```

```
