from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrganizationCreationForm
from superadmin.models import UserProfile
from .models import Organization
from django.http import HttpResponseRedirect
from django.urls import reverse


def create_organization(request):
    if request.method == 'POST':
        form = OrganizationCreationForm(request.POST)
        if form.is_valid():
            organization = form.save(commit=False)
            organization.superadmin = request.user
            organization.save()
            return redirect('organization_profile')
    else:
        form = OrganizationCreationForm()

    return render(request, 'create_organization.html', {'form': form})


def organization_profile(request):
    organizations = Organization.objects.all()
    return render(request, 'organization_profile.html', {'organizations': organizations})

def update_organization(request, pk):
    organization = get_object_or_404(Organization, pk=pk)

    if request.method == 'POST':
        form = OrganizationCreationForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()
            return redirect('organization_profile')
    else:
        form = OrganizationCreationForm(instance=organization)

    return render(request, 'update_organization.html', {'form': form, 'organization': organization})

def delete_organization(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    
    if request.method == 'POST':
        organization.delete()
        return redirect('organization_profile')

    return render(request, 'delete_organization.html', {'organization': organization})