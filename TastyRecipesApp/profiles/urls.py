from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_profile, name='create_profile'),
    path('edit/<int:profile_id>/', views.edit_profile, name='edit_profile'),
    path('details/', views.profile_details, name='profile_details'),
    path('delete/', views.delete_profile, name='delete_profile'),
]
