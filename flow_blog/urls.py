from django.urls import path
from .models import BlogPost
from .views import BlogPageView, BlogDetailView

urlpatterns = [
    path('', BlogPageView.as_view(), name='blog_page'),
    path('', BlogDetailView.as_view(), name='blog_details'),
]
