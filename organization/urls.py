from django.urls import path
from .views import create_organization, organization_profile, update_organization, delete_organization, organization_home

urlpatterns = [
    path('create/', create_organization, name='create_organization'),
    path('profile/', organization_profile, name='profile'),
    path('home/<uuid:pk>/', organization_home, name='organization_home'),
    path('update_organization/<uuid:pk>/', update_organization, name='update_organization'),
    path('delete_organization/<uuid:pk>/', delete_organization, name='delete_organization'),
]
