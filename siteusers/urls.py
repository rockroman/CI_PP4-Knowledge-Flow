from django.urls import path
from .views import ProfieView


urlpatterns = [
    path('', ProfieView.as_view(), name='profile'),
    
]