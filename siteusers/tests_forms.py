from django.test import TestCase, Client 
from .models import Profile, User
from .forms import Profileform
from categories.models import LearningCategory
from django.contrib.auth.models import AnonymousUser


class TestProfileForm(TestCase):
    @classmethod
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='testRock',
            password='mynewpass',
            id='11'

        )
        self.user.save()
        self.user.set_password('mynewpass')
        self.user.save()
        self.user_profile = Profile.objects.update(
            user=self.user,
            first_name='Rock',
            last_name='Roman',
            email='test@user11.com',
            bio='my biography',
            role='student',

        )

    
    # def test_saving_of_email(self):
    #     self.client.login(username='testRock', password='mynewpass')
    #     # profile = Profile.objects.get(user=self.user.id)
    #     category = LearningCategory.objects.create(
    #         maker=User.objects.get(username='testRock'),
    #         name='test category'
    #     )
    #     response = self.client.post('/siteusers/edit_profile/', data={
    #         'first_name': 'Rock',
    #         'last_name': 'Roman',
    #         'email': 'rock.roman@bo.com',
    #         'bio': 'my new bio',
    #         'category': category
    #     })
    #     form = response.context['form']
    #     print(form.errors)
    #     # self.assertTrue(self.user.email=='test@user11.com')
    #     # self.assertEqual(response.status_code, 200)
    #     # self.assertEqual(self.user.email, 'mi')
