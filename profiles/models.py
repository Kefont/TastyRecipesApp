from django.db import models

class Profile(models.Model):
    nickname = models.CharField(max_length=20, unique=True, error_messages={"unique": "Nickname must be unique!", "min_length": "Nickname must be at least 2 chars long!"})
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    chef = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nickname
