from django.urls import path
from .models import BlogPost, Comment
from . import views
from .views import (
    BlogPageView, BlogDetailView,
    AddBlogView, UpdateBlogView, DeleteBlogView,
    delete_comment
    )

urlpatterns = [
    path('', BlogPageView.as_view(), name='blog_page'),
    path('blog/blog/<int:pk>', BlogDetailView.as_view(), name='blog_details'),
    path('blog/add_blog/', AddBlogView.as_view(), name='add_blog'),
    path(
        'blog/edit_blog/<int:pk>', UpdateBlogView.as_view(), name='edit_blog'),
    path(
        'blog/delete_blog/<int:pk>',
        DeleteBlogView.as_view(), name='delete_blog'),
    # path('blog/blog/<int:pk>/comment/<int:pkc>/delete', CommentDeleteView.as_view(), name='comment_delete')
    # path('blog/comment/<int:pk>/delete', views.delete_comment, name='delete_comment')
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
