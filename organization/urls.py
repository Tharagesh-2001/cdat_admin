from django.urls import path
from .views import create_organization

urlpatterns = [
    path('create/', create_organization, name='create_organization'),
]
