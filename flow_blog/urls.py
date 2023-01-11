from django.urls import path
from .models import BlogPost
from .views import BlogPageView, BlogDetailView, AddBlogView, UpdateBlogView, DeleteBlogView

urlpatterns = [
    path('', BlogPageView.as_view(), name='blog_page'),
    path('blog/blog/<int:pk>', BlogDetailView.as_view(), name='blog_details'),
    path('blog/add_blog/', AddBlogView.as_view(), name='add_blog'),
    path('blog/edit_blog/<int:pk>', UpdateBlogView.as_view(), name='edit_blog'),
    path('blog/delete_blog/<int:pk>', DeleteBlogView.as_view(), name='delete_blog'),
]
