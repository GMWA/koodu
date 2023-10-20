from flask_restful import Api
from .users.controllers import UsersController, UserController
from .posts.controllers import PostsController, PostController


api = Api()


def create_module(app):
    api.add_resource(UsersController, "/api/users")
    api.add_resource(UserController, "/api/users/<int:user_id>")
    api.add_resource(PostsController, "/api/users")
    api.add_resource(PostController, "/api/users/<int:post_id>")

    api.init_app(app)
    app.logger.info("REST API module loaded.")