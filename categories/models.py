from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from siteusers.models import Profile


# Create your models here.
class LearningCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()