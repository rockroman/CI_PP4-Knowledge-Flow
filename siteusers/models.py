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
    image = CloudinaryField('image', default='placeholder')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    website_url = models.URLField(max_length=100, default='https://www.google.com/')
    # linkedIn_url = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000)
    role = models.CharField(max_length=20, choices=ROLE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return f'{self.user.username} Profile'

    
