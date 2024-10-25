from django.contrib import admin
from django.urls import include, path

from profiles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('profile/', include('TastyRecipesApp.profiles.urls')),  # include profile URLs
    path('recipe/', include('TastyRecipesApp.recipes.urls')),    # include recipe URLs
]
