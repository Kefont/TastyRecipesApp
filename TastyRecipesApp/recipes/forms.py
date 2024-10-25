from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url']
        help_texts = {
            'ingredients': 'Ingredients must be separated by a comma and space.',
            'cooking_time': 'Provide the cooking time in minutes.',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Recipe.objects.filter(title=title).exists():
            raise forms.ValidationError("We already have a recipe with the same title!")
        return title
