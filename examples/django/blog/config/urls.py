from django.contrib import admin
from django.urls import path, include
from blog_api import urls as blog_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("blogs/", include(blog_urls)),
]