import os
from flask import abort, request
from flask_restful import Resource
from todo import db
from todo.models import User
from todo.models import Category
from todo.models import Todo


class UsersController(Resource):
    def get(self):
        return User.query.all()

    def post(self):
        name = request.args.get("name", None)
        email = request.args.get("email", None)
        username = request.args.get("username", None)
        password = request.args.get("password", None)
        user = User()
        user.name = name
        user.email = email
        user.username = username
        user.password = password
        db.session.add(user)
        db.session.commit()


class UserController(Resource):
    def get(self, user_id):
        db_user = User.query.get(user_id)
        if not db_user:
            abort(404)
        return db_user

    def put(self, user_id):
        db_user = User.query.get(user_id)
        if not db_user:
            abort(404)
        name = request.args.get("name", None)
        email = request.args.get("email", None)
        username = request.args.get("username", None)
        password = request.args.get("password", None)
        db_user.name = name
        db_user.email = email
        db_user.username = username
        db_user.password = password
        db.session.commit()

    def delete(self, user_id):
        db_user = User.query.get(user_id)
        if not db_user:
            abort(404)

        db.session.delete(db_user)
        db.session.commit()