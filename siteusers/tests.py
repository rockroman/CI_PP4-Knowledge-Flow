from django.test import TestCase
from .models import Profile, User
from django.contrib.auth import get_user_model


# # Create your tests here.


class TestSiteusersModels(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
                username='testuser',
                password='secret')
        self.profile = Profile.objects.update(
            user=self.user,
        )

    def test_is_profile_created(self):
        profile = Profile.objects.filter().last()
        self.assertEquals(profile.user.username, 'testuser')
