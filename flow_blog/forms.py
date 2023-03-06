"""
flow_blog forms module
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
# from cloudinary.models import CloudinaryField
# from cloudinary.forms import CloudinaryFileField
# Internal:
from .models import BlogPost, Comment
from siteusers.models import LearningCategory, Profile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class BlogForm(forms.ModelForm):
    """
    A class for the blog creation form
    """

    class Meta:
        model = BlogPost
        fields = ('title', 'cover_image', 'category', 'body')

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }

    def __init__(self, user=True, **kwargs):
        """
        Link category choice from the profile form
        to blog form
        """
        super(BlogForm, self).__init__(**kwargs)
        current_user = Profile.objects.get(user=user)
        self.fields['category'].queryset = current_user.category.all()


class CommentForm(forms.ModelForm):

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'md-textarea form-control comment-text',
                'placeholder': 'your comment....',
                'rows': '3',
                'id': 'comment',


            }
        ),
        label='comment:'
    )

    class Meta:
        model = Comment
        fields = ['content']


class UpdateCommentForm(forms.ModelForm):

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'md-textarea form-control comment-text',
                'placeholder': 'your comment....',
                'rows': '3',

            }
        ),
        label=''
    )

    class Meta:
        model = Comment
        fields = ['content']
