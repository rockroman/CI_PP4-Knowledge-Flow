from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
# Create your models here.


class Profile(models.Model):
    ROLE = (
        ('Mentor', 'Mentor'),
        ('Student', 'Student')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, unique=True,null=True)
    image = CloudinaryField('image', default='placeholder')
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, null=True)
    bio = models.TextField(max_length=1000, blank=True)
    role = models.CharField(max_length=20, choices=ROLE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return f'{self.user.username} Profile'

    
