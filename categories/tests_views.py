"""
Category views test module
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client, RequestFactory
# Internal:
from .views import LearningCategoryListView
from .models import LearningCategory, User
from flow_blog.models import BlogPost
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCategoryView(TestCase):
    @classmethod
    def setUp(self):
        """
        creating and saving a new test user
        """
        self.user = User.objects.create(
            username='testUser00',
            password='mypass7999',
            email='test@user99.com',
            id='10',

        )
        self.user.save()
        """
        creating test category
        """
        self.test_category = LearningCategory.objects.create(
            maker=self.user,
            name='Reading',
            start_quote='Reading is the key'
        )
        self.test_category.save()
        post = BlogPost.objects.filter(category__name=self.test_category.name)

    def tearDown(self):
        self.test_category.delete()
        self.user.delete()

    def test_the_queryset_return(self):
        """
        creating the client
        """
        self.factory = RequestFactory()
        request = self.factory.get('category/<category>/')
        """
        instantiating a view
        """
        view = LearningCategoryListView()
        view.kwargs = {'category': 'test_category'}
        qs = view.get_queryset()
        self.assertEqual(qs['cat'], 'test_category')

    def test_is_the_right_template_used(self):

        client = Client()
        response = client.get('category/<category>/')
        self.assertTemplateUsed(
                'accounts/login/?next=/categories/category/Leadership/')
