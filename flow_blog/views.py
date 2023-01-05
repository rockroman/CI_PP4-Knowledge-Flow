from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost


# Create your views here.
class BlogPageView(ListView):
    model = BlogPost
    context_object_name = 'blog_post'
    template_name = 'flow_blog/blog.html'
