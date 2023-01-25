from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from . models import LearningCategory
from flow_blog.models import BlogPost

# Create your views here.


class LearningCategoryListView(ListView):
    template_name = 'categories/category.html'
    context_object_name = 'cat_list'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': BlogPost.objects.filter(category__name=self.kwargs['category'])
        }
        return content
