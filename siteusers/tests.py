from django.test import TestCase
from .models import Profile, User
from django.contrib.auth import get_user_model


# # Create your tests here.


class TestSiteusersModel(TestCase):

    @classmethod
    def setUp(self):
        # Create test user
        self.user = User.objects.create(
            username='MyTestUser',
            password='mypass79',
            email='test@user.com',
            id='1',
        )
        self.user.save()

        self.user_profile = Profile.objects.update(
            user=self.user,
            first_name='miki'

        )

    def test_is_profile_created(self):
        # profile created is empty except user.username  until updating
        user_profile = Profile.objects.filter().last()
        self.assertEquals(user_profile.user.username, 'MyTestUser')
        self.assertEquals(user_profile.first_name, 'miki')
        self.assertEquals(user_profile.bio, '')
        
