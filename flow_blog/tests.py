from django.test import TestCase, Client
from siteusers.models import Profile, User
from .models import BlogPost


# Create your tests here.
class TestBlogModel(TestCase):

    def test_string_method(self):
        test_user = User.objects.create(username='miki')
        blog = BlogPost.objects.create(
            title='test title',
            creator=test_user,
        )
        self.assertEqual(str(blog), 'test title | miki')


