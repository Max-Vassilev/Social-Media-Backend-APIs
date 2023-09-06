from django.db import models
from django.contrib.auth import models as auth_models


class SocialMediaUser(auth_models.AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField()
    profile_picture = models.ImageField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.email
