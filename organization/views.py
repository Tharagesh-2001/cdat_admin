from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import OrganizationCreationForm
from superadmin.models import UserProfile
from .models import Organization

def organization_profile(request):
    organizations = Organization.objects.all()
    return render(request, 'organization_profile.html', {'organizations': organizations})

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

def update_organization(request, pk):
    organization = get_object_or_404(Organization, pk=pk)

    if request.method == 'POST':
        form = OrganizationCreationForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()
            return redirect('organization_home', pk=organization.pk)
    else:
        form = OrganizationCreationForm(instance=organization)

    return render(request, 'update_organization.html', {'form': form, 'organization': organization})

def delete_organization(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    
    if request.method == 'POST':
        organization.delete()
        return redirect('organization_home', pk=organization.pk)

    return render(request, 'delete_organization.html', {'organization': organization})

def organization_home(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    return render(request, 'organization_home.html', {'organization': organization})