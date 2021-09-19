from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=20)
    university = models.CharField(max_length=30)
    location = models.CharField(max_length=20)
    like_posts = models.ManyToManyField("blogapp.Blog", blank=True, related_name='like_users')
    

