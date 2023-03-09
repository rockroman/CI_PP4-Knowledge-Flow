"""
 module for home urls
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path
from . import views
# Internal:
from .views import home


urlpatterns = [
    path('', views.home, name='home'),

]
