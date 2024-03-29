"""
A module for flow_blog models
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
# Internal:
from siteusers.models import LearningCategory
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class BlogPost(models.Model):
    """
    BlogPost model used for each
    blog uploaded by the user
    """
    title = models.CharField(max_length=200, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        LearningCategory, on_delete=models.PROTECT, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    cover_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title + ' | ' + str(self.creator)

    def get_absolute_url(self):
        return reverse("blog_page")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    """
     model for users Comments
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    blogpost = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=500)
    status = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('blog_details', kwargs={'pk': self.blogpost.pk})

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.author.username + '|comment on ' + self.blogpost.title
