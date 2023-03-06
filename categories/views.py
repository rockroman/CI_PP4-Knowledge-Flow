"""
A module for views
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
# Internal:
from . models import LearningCategory
from flow_blog.models import BlogPost
from siteusers.models import Profile
from django.views.generic import ListView
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class LearningCategoryListView(LoginRequiredMixin, ListView):
    """
    A class view to view alist all the categories
    """
    template_name = 'categories/category.html'
    context_object_name = 'cat_list'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': BlogPost.objects.filter(
                category__name=self.kwargs['category'])
        }
        return content


def list_of_categories(request):
    """
    view that serves as a context processor
    and makes categories of objects available throughout
    all templates
    """
    category_list = LearningCategory.objects.all()
    context = {
        'category_list': category_list
    }
    return context
