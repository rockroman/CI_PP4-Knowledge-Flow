from django.urls import path
from .views import ProfilePageView
from . import views


urlpatterns = [
    path('', ProfilePageView.as_view(), name='myprofile'),
    # path('', views.UserProfilePage, name='profile'),
    
]