from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_recipe, name='create_recipe'),
    path('edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('catalogue/', views.catalogue, name='catalogue'),  # Show all recipes
    path('<int:recipe_id>/details/', views.recipe_details, name='recipe_details'),  # View recipe details
    path('<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),  # Delete recipe
]
