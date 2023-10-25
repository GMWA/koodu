from django.urls import path
from .views import (
    PostListApiView,
    PostDetailApiView,
)

urlpatterns = [
    path('api', PostListApiView.as_view()),
    path('api/<int:post_id>/', PostDetailApiView.as_view()),
]