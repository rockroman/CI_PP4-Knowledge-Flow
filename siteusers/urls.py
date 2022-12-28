from django.urls import path
from .views import CreateProfileView, SeeProfilePageView
from . import views


urlpatterns = [
    path('create_profile/',
         CreateProfileView.as_view(), name='create_myprofile'),
    path('<int:pk>/profile', SeeProfilePageView.as_view(), name='myprofile'),
    
]