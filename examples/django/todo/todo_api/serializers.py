from rest_framework import serializers
from .models import (
    Category,
    Todo,
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name","description",]class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["title","description","category_id","user_id",]