"""
A module for testing models
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
# Internal:
from .models import LearningCategory, User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestLearningCategoryModel(TestCase):
    @classmethod
    def setUp(self):
        """
        creating and saving a new test user
        """
        self.user = User.objects.create(
            username='NewTestUser',
            password='mypass7900',
            email='test@user.com',
            id='0',

        )
        self.user.save()

    def tearDown(self):
        """
        deleting a test user
        """
        LearningCategory.objects.filter(maker=self.user).delete()
        self.user.delete()

    def test_string_method_returning_name(self):
        """
        creating a category object
        """
        new_category = LearningCategory.objects.create(
            maker=self.user,
            name='Coding',
            start_quote='Coding is an amazing skill'
        )
        self.assertEquals(str(new_category), 'Coding')
