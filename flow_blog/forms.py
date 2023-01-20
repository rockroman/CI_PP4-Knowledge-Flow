from django import forms
from .models import BlogPost, Comment
from cloudinary.models import CloudinaryField
from cloudinary.forms import CloudinaryFileField 

# ---3rd party ----------


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'cover_image', 'body')

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }


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
