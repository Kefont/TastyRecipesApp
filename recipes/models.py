from django.db import models
from profiles.models import Profile

class Recipe(models.Model):
    CUISINE_CHOICES = [
        ('French', 'French'),
        ('Chinese', 'Chinese'),
        ('Italian', 'Italian'),
        ('Balkan', 'Balkan'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=100, unique=True, error_messages={"unique": "We already have a recipe with the same title!"})
    cuisine_type = models.CharField(max_length=7, choices=CUISINE_CHOICES)
    ingredients = models.TextField(help_text="Ingredients must be separated by a comma and space.")
    instructions = models.TextField()
    cooking_time = models.PositiveIntegerField(help_text="Provide the cooking time in minutes.")
    image_url = models.URLField(blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
