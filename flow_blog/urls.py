from django.urls import path
from .models import BlogPost
from .views import BlogPageView

urlpatterns = [
    path('', BlogPageView.as_view(), name='blog_page'),
]
