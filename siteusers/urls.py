from django.urls import path
from .views import AppUserSetUpProfile,AppUserCreateProfile, SeeProfilePageView, EditProfilePageView, DeleteProfileView, redirect_view   # CreateProfileView, 
from . import views


urlpatterns = [
    path('create_profile/', AppUserSetUpProfile.as_view(), name='appuser_SetUp_profile'),
    path('create_profile/', AppUserCreateProfile.as_view(), name='appuser_create_profile'),
    path('see_profile/', SeeProfilePageView.as_view(), name='see_profile'),
    path('edit_profile/', EditProfilePageView.as_view(), name='edit_profile'),
    path('delete_profile/', DeleteProfileView.as_view(), name='delete_profile'),
    path('redirect/', views.redirect_view, name='redirect'),
    
    
    
]