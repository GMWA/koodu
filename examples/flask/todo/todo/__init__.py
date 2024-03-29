import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from configs import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
cors = CORS(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


from todo.api import create_module as api_create_module

api_create_module(app)