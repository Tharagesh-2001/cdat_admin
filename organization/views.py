from django.shortcuts import render, redirect
from .forms import OrganizationCreationForm
from superadmin.models import UserProfile

def create_organization(request):
    if request.method == 'POST':
        form = OrganizationCreationForm(request.POST)
        if form.is_valid():
            organization = form.save(commit=False)
            organization.superadmin = request.user
            organization.save()
            return redirect('organization_detail', pk=organization.pk)
    else:
        form = OrganizationCreationForm()

    return render(request, 'create_organization.html', {'form': form})
