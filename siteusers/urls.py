from django.urls import path
from .views import AppUserProfile, SeeProfilePageView                       #EditProfilePageView, CreateProfileView, 
from . import views


urlpatterns = [
    path('profile/', AppUserProfile.as_view(), name='appuser_profile'),
    path('profile/', AppUserProfile.as_view(), name='appuser_profile'),
    
    
    
]