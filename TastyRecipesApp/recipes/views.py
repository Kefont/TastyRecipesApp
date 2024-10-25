from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import Recipe


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user.profile  # Assuming user has a profile
            recipe.save()
            return redirect('catalogue')
    else:
        form = RecipeForm()
    return render(request, 'templates/create-recipe.html', {'form': form})

def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_details', recipe_id=recipe_id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'templates/edit-recipe.html', {'form': form})
