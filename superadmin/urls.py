from django.urls import path
from .views import register, user_login, user_logout, home
from organization.views import create_organization, organization_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('home/', home, name='home'),

    path('create_organization/', create_organization, name='create_organization'),
    path('organization_profile/', organization_profile, name='organization_profile'),
]
