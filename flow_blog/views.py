from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogPost


# Create your views here.
class BlogPageView(ListView):
    model = BlogPost
    context_object_name = 'blog_post'
    template_name = 'flow_blog/blog.html'


class BlogDetailView(DetailView):

    model = BlogPost
    context_object_name = 'post'
    template_name = 'flow_blog/blog_details.html'


class AddBlogView(CreateView):

    model = BlogPost
    template_name = 'add_blog.html'
    fields = [
        'title', 'cover_image', 'body'
    ]

