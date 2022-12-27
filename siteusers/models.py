from django.db import models
from django.contrib.auth.models import User
# from django.urls import reverse
from cloudinary.models import CloudinaryField
# Create your models here.


class Profile(models.Model):
    ROLE = (
        ('Mentor', 'Mentor'),
        ('Student', 'Student')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='placeholder')
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(max_length=1000, blank=True)
    role = models.CharField(max_length=20, choices=ROLE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return reverse('home', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.user.username} Profile'

    
