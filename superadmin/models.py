from django.contrib.auth.models import AbstractUser
from django.db import models
from organization.models import Organization

class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    organizations = models.ManyToManyField('organization.Organization', related_name='admins')