from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    cover_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' | ' + self.creator
