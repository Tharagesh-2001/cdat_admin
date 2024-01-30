# organization/forms.py
from django import forms
from .models import Organization

class OrganizationCreationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['organization_name', 'email', 'username', 'password']
