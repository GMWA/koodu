import os
from flask import abort, request
from flask_restful import Resource
from blog import db
from blog.models import User
from blog.models import Post


class PostsController(Resource):
    def get(self):
        return Post.query.all()

    def post(self):
        title = request.args.get("title", None)
        text = request.args.get("text", None)
        user_id = request.args.get("user_id", None)
        post = Post()
        post.title = title
        post.text = text
        post.user_id = user_id
        db.session.add(post)
        db.session.commit()


class PostController(Resource):
    def get(self, post_id):
        db_post = Post.query.get(post_id)
        if not db_post:
            abort(404)
        return db_post

    def put(self, post_id):
        db_post = Post.query.get(post_id)
        if not db_post:
            abort(404)
        title = request.args.get("title", None)
        text = request.args.get("text", None)
        user_id = request.args.get("user_id", None)
        db_post.title = title
        db_post.text = text
        db_post.user_id = user_id
        db.session.commit()

    def delete(self, post_id):
        db_post = Post.query.get(post_id)
        if not db_post:
            abort(404)

        db.session.delete(db_post)
        db.session.commit()