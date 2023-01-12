from django.urls import path
from .views import (
    AppUserSetUpProfile,
    SeeProfilePageView,
    EditProfilePageView,
    DeleteAppUser,
    SetProfileRole)
from . import views


urlpatterns = [
    path(
        'create_profile/', AppUserSetUpProfile.as_view(),
        name='appuser_SetUp_profile'),
    path('see_profile/', SeeProfilePageView.as_view(), name='see_profile'),
    path('edit_profile/', EditProfilePageView.as_view(), name='edit_profile'),
    path('delete_profile/', DeleteAppUser.as_view(), name='delete_profile'),
    path('redirect/', views.redirect_view, name='redirect'),
    path('set_role/', views.SetProfileRole, name='set_role'),
    path(
        'protect_profile/',
        views.protect_profile_view, name='protect_profile'),

]
