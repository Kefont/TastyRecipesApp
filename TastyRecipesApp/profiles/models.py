from django.db import models
from django.core.exceptions import ValidationError


class Profile(models.Model):
    nickname = models.CharField(
        max_length=20,
        unique=True,
        error_messages={
            "unique": "Nickname must be unique!",
            "min_length": "Nickname must be at least 2 chars long!"
        }
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    chef = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)

    def clean(self):
        # Custom validation for first name starting with a capital letter
        if not self.first_name[0].isupper():
            raise ValidationError("First Name must start with a capital letter!")

        # Custom validation for last name starting with a capital letter
        if not self.last_name[0].isupper():
            raise ValidationError("Last Name must start with a capital letter!")

    def __str__(self):
        return self.nickname
