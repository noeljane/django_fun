from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Startup(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.TextField()
    description = models.TextField()
    photo = models.TextField()
    photo_attribute = models.TextField(blank=True)
    photo_photographer = models.TextField(blank=True)
    photo_profile_link = models.TextField(blank=True)
    founder = models.ForeignKey(User, on_delete=models.CASCADE)

    likes = models.IntegerField(default=1)
    founded_date = models.DateTimeField(default=timezone.now)
