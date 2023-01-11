from django import forms
from .models import BlogPost
from cloudinary.models import CloudinaryField

# ---3rd party ----------
from image_uploader_widget.widgets import ImageUploaderWidget


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'cover_image', 'creator', 'body')

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
            'creator': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }
