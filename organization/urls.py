from django.urls import path
from .views import create_organization, organization_profile, update_organization, delete_organization

urlpatterns = [
    path('create/', create_organization, name='create_organization'),
    path('profile/<uuid:pk>/', organization_profile, name='profile'),
    path('update_organization/<uuid:pk>/', update_organization, name='update_organization'),
    path('delete_organization/<uuid:pk>/', delete_organization, name='delete_organization'),
]
