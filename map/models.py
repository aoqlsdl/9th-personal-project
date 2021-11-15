from django.db import models

# Create your models here.
class Tourism(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50, default="")
    latitude = models.FloatField(default=0.0)
    longtitude = models.FloatField(default=0.0)