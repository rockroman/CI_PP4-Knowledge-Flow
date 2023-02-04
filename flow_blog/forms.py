from django import forms
from django.contrib.auth.models import User
from .models import BlogPost, Comment
from cloudinary.models import CloudinaryField
from cloudinary.forms import CloudinaryFileField
from siteusers.models import Profile
from crispy_forms.helper import FormHelper
from siteusers.models import LearningCategory, Profile

# ---3rd party ----------

class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'cover_image', 'category', 'body')

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }

    def __init__(self, user=True, **kwargs):
        super(BlogForm, self).__init__(**kwargs)
        current_user = Profile.objects.get(user=user)
        self.fields['category'].queryset = current_user.category.all()


# class BlogForm(forms.ModelForm):

#     class Meta:
#         model = BlogPost
#         fields = ('title', 'cover_image', 'category', 'body')

#         widgets = {
#             'title': forms.TextInput(
#                 attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
#             'body': forms.Textarea(attrs={'class': 'form-control'}),

#         }

#     def __init__(self, user=None, **kwargs):
#         super(BlogForm, self).__init__(**kwargs)
#         current_user = Profile.objects.get(user=user)
#         self.fields['category'].queryset = current_user.category.all()


class CommentForm(forms.ModelForm):

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'md-textarea form-control',
                'placeholder': 'your comment....',
                'rows': '3',
                'id': 'comment-text',

            }
        )
    )

    class Meta:
        model = Comment
        fields = ['content',]
