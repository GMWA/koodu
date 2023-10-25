from django.urls import path
from .views import (
    CategoryListApiView,
    CategoryDetailApiView,
    TodoListApiView,
    TodoDetailApiView,
)

urlpatterns = [
    path('api', CategoryListApiView.as_view()),
    path('api/<int:category_id>/', CategoryDetailApiView.as_view()),
    path('api', TodoListApiView.as_view()),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
]