from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm

def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user.profile  # Assuming a logged-in user has a profile
            recipe.save()
            return redirect('catalogue')
    else:
        form = RecipeForm()
    return render(request, 'create-recipe.html', {'form': form})

# Define other views for recipe details, edit, and delete
