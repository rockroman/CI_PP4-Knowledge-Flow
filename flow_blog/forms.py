from django import forms
from .models import BlogPost


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'cover_image', 'creator', 'body')
