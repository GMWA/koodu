from flask_restful import Api
from .users.controllers import UsersController, UserController
from .categorys.controllers import CategorysController, CategoryController
from .todos.controllers import TodosController, TodoController


api = Api()


def create_module(app):
    api.add_resource(UsersController, "/api/users")
    api.add_resource(UserController, "/api/users/<int:user_id>")
    api.add_resource(CategorysController, "/api/users")
    api.add_resource(CategoryController, "/api/users/<int:category_id>")
    api.add_resource(TodosController, "/api/users")
    api.add_resource(TodoController, "/api/users/<int:todo_id>")

    api.init_app(app)
    app.logger.info("REST API module loaded.")