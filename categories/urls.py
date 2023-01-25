from django.urls import path
from . import views
from .models import LearningCategory


urlpatterns = [
    path('category/<category>/', views.LearningCategoryListView.as_view(), name='category')

]
