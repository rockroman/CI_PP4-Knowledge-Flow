from django.test import TestCase, Client, RequestFactory
from .views import LearningCategoryListView
from .models import LearningCategory, User
from flow_blog.models import BlogPost


class TestCategoryView(TestCase):
    def setUp(self,**kwargs):
        # creating and saving a new test user

        self.user = User.objects.create(
            username='testUser00',
            password='mypass7999',
            email='test@user99.com',
            id='10',

        )
        self.user.save()
        # creating test category
        test_category = LearningCategory.objects.create(
            maker=self.user,
            name='Reading',
            start_quote='Reading is the key'
        )
        test_category.save()
        # content = {
        #     'cat': 'Reading',
        #     'posts': BlogPost.objects.filter(category__name='Reading')
        # }        
        # post = BlogPost.objects.filter(category__name='Reading') 


        
    # def test_the_response_code(self):
    #     # creating a client
    #     self.factory = RequestFactory()
    #     request = self.factory.get('category/<category>/')
    #     request.user = self.user
    #     # qs = LearningCategoryListView.get_queryset(self)
    #     response = LearningCategoryListView.as_view()(request)
    #     self.assertEqual(response., 2)
        

    def test_is_the_right_template_used(self):
        # creating a client
        client = Client()
        response = client.get('category/<category>/')
        self.assertTemplateUsed('categories/category.html')
