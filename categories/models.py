"""
A module for Categories models
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class LearningCategory(models.Model):
    """
    Categories model used as a choice of every
    user to learn from and write about it
    """
    maker = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    category_image = CloudinaryField('image', default='placeholder')
    start_quote = models.CharField(max_length=255, null=True)
    description = models.TextField()
    importance_of_category = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}'
