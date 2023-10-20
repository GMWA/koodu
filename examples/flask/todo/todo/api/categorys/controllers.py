import os
from flask import abort, request
from flask_restful import Resource
from todo import db
from todo.models import User
from todo.models import Category
from todo.models import Todo


class CategorysController(Resource):
    def get(self):
        return Category.query.all()

    def post(self):
        name = request.args.get("name", None)
        description = request.args.get("description", None)
        category = Category()
        category.name = name
        category.description = description
        db.session.add(category)
        db.session.commit()


class CategoryController(Resource):
    def get(self, category_id):
        db_category = Category.query.get(category_id)
        if not db_category:
            abort(404)
        return db_category

    def put(self, category_id):
        db_category = Category.query.get(category_id)
        if not db_category:
            abort(404)
        name = request.args.get("name", None)
        description = request.args.get("description", None)
        db_category.name = name
        db_category.description = description
        db.session.commit()

    def delete(self, category_id):
        db_category = Category.query.get(category_id)
        if not db_category:
            abort(404)

        db.session.delete(db_category)
        db.session.commit()