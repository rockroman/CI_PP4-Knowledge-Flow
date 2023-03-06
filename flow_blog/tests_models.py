"""
A module for testing models
"""
from django.test import TestCase, Client
from siteusers.models import Profile, User
from .models import BlogPost, Comment


# Create your tests here.
class TestBlogModel(TestCase):

    def test_string_method(self):
        test_user = User.objects.create(username='miki')
        blog = BlogPost.objects.create(
            title='test title',
            creator=test_user,
        )
        self.assertEqual(str(blog), 'test title | miki')

    def test_get_absolute_url(self):
        test_user = User.objects.create(username='Rock')
        blog = BlogPost.objects.create(
            title='test title',
            creator=test_user,
            cover_image='placeholder'
        )
        client = Client()
        response = client.get(blog.get_absolute_url())
        self.assertEqual(response.status_code, 200)


class TestCommentModel(TestCase):

    def test_model_string_method(self):
        test_user = User.objects.create(username='miki')
        blog = BlogPost.objects.create(
            title='New Title',
            creator=test_user,
        )
        comment = Comment.objects.create(
            author=test_user,
            blogpost=blog,
            content='my new blog'

        )
        client = Client()
        response = client.get('')
        self.assertEqual(str(comment), 'miki|comment on New Title')

 