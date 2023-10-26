import os
from flask import abort, request
from flask_restful import Resource
from todo import db
from todo.models import User
from todo.models import Category
from todo.models import Todo


class TodosController(Resource):
    def get(self):
        return Todo.query.all()

    def post(self):
        title = request.args.get("title", None)
        description = request.args.get("description", None)
        category_id = request.args.get("category_id", None)
        user_id = request.args.get("user_id", None)
        todo = Todo()
        todo.title = title
        todo.description = description
        todo.category_id = category_id
        todo.user_id = user_id
        db.session.add(todo)
        db.session.commit()


class TodoController(Resource):
    def get(self, todo_id):
        db_todo = Todo.query.get(todo_id)
        if not db_todo:
            abort(404)
        return db_todo

    def put(self, todo_id):
        db_todo = Todo.query.get(todo_id)
        if not db_todo:
            abort(404)
        title = request.args.get("title", None)
        description = request.args.get("description", None)
        category_id = request.args.get("category_id", None)
        user_id = request.args.get("user_id", None)
        db_todo.title = title
        db_todo.description = description
        db_todo.category_id = category_id
        db_todo.user_id = user_id
        db.session.commit()

    def delete(self, todo_id):
        db_todo = Todo.query.get(todo_id)
        if not db_todo:
            abort(404)

        db.session.delete(db_todo)
        db.session.commit()