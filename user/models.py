from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(max_length=64, unique=True)

    last_name = models.CharField(max_length=64, unique=True)
    first_name = models.CharField(max_length=64, unique=True)



