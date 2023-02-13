from django.test import TestCase, Client
from siteusers.models import Profile, User
from .models import BlogPost, Comment
from .forms import BlogForm

class TestBlogForm(TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='testRock',
            password='mynewpass',
            email='test.rock@bo.com',

        )
        self.user_profile = Profile.objects.update(
            user=self.user,
            first_name='Rock',
            last_name='Roman',
            email='test@user11.com',
            bio='my biography',
            role='Student'

        )        

        self.post = BlogPost.objects.create(
            creator= self.user,
            title='my test',
            body='My test text',
            cover_image='placeholder'
        )

    def test_that_title_is_required(self):
        form = BlogForm(data= {'title': ''})
        self.assertFalse(form.is_valid())

