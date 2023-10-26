from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 255)
    text = models.CharField(max_length = 1000)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    
    def __str__(self):
        return self.id