from django.urls import path
from .views import AppUserProfile, SeeProfilePageView, EditProfilePageView, DeleteProfileView   # CreateProfileView, 
from . import views


urlpatterns = [
    path('create_profile/', AppUserProfile.as_view(), name='appuser_profile'),
    path('see_profile/', SeeProfilePageView.as_view(), name='see_profile'),
    path('edit_profile/', EditProfilePageView.as_view(), name='edit_profile'),
    path('delete_profile/', DeleteProfileView.as_view(), name='delete_profile'),
    
    
    
]