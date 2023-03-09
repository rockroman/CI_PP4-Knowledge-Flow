"""
A module for testing models
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client, RequestFactory
# Internal:
from .models import Profile, User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestSiteusersModel(TestCase):

    @classmethod
    def setUp(self):
        """
        creating and saving a new test user
        """
        self.user = User.objects.create(
            username='MyTestUser',
            password='mypass79',
            email='test@user.com',
            id='1',
        )
        self.user.save()

        self.user_profile = Profile.objects.update(
            user=self.user,
            first_name='miki',
        )

    def test_is_profile_created(self):
        """
        profile created is empty except
        user.username  until updating
        """
        user_profile = Profile.objects.filter().last()
        self.assertEquals(user_profile.user.username, 'MyTestUser')
        self.assertEquals(user_profile.first_name, 'miki')
        self.assertEquals(user_profile.bio, '')

    def test_profile_string_method_returning_username(self):
        user = User.objects.create(
            username='test_user_2',
            password='mypass799',
            email='test@user2.com',
            id='2',
        )
        user.save()
        user_profile = Profile.objects.get(user=user)
        self.assertEqual(str(user_profile), 'test_user_2')

    def test_get_absolute_url(self):
        client = Client()
        user = User.objects.create(
            username='test_user_2',
            password='mypass799',
            email='test@user2.com',
            id='2',
        )
        user.save()
        user_profile = Profile.objects.get(user=user)
        response = client.get(user_profile.get_absolute_url())
        self.assertEqual(response.status_code, 200)
