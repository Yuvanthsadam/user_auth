from django.contrib.auth.models import AbstractUser
from djongo import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
