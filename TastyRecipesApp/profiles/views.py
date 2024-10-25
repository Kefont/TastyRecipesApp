from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')  # Adjust the redirect URL
    else:
        form = ProfileForm()
    return render(request, 'templates/create-profile.html', {'form': form})

def edit_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'templates/edit-profile.html', {'form': form})

def home(request):
    return render(request, 'templates/home-page.html')

