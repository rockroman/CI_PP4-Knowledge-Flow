from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class LearningCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'