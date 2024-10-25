from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileForm()
    return render(request, 'create-profile.html', {'form': form})

# Define other views similarly for profile details, edit, and delete
