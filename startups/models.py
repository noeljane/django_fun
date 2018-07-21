from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Startup(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.TextField()
    photo = models.TextField()
    founder = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=1)
