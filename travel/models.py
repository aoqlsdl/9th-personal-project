from django.db import models
from django.forms import ModelForm
from django.db.models.base import Model
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# from taggit.managers import TaggableManager
from taggit.models import (
    TagBase
)

# Create your models here.
class HashTag(models.Model):
    hashtag_name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.hashtag_name 

class Record(models.Model):
    title = models.CharField(max_length=200, default='')
    pub_date = models.DateTimeField('date published')
    body = models.TextField(default='')
    hashtag = models.ManyToManyField(HashTag, default='')
    image = models.ImageField(upload_to = 'images/', blank = True, null = True)
    # user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="record", default='', null=True)
    like_users = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    post = models.ForeignKey(Record, related_name="comments", on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20, default='')
    comment_text = models.TextField()
    comment_date = models.DateTimeField(default = timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.comment_text

class MyPage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'images/', null = True)
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.title

class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    post = models.ForeignKey(Record, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null = True, blank = True, upload_to = "travel/")
    hashtag_name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.title

# TagBase를 상속받은 tag model
class Tag(TagBase):

    slug = models.SlugField(
        verbose_name='slug',
        unique=True,
        max_length=100,
        allow_unicode=True,
    )

