from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 128)
    description = models.CharField(max_length = 1000)
    
    def __str__(self):
        return self.idclass Todo(models.Model):
    title = models.CharField(max_length = 255)
    description = models.CharField(max_length = 1000)
    category_id = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    
    def __str__(self):
        return self.id