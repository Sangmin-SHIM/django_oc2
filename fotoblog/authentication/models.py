from django.contrib.auth.models import AbstractUser
from django.db import models
from authentication.constants import RoleType


class User(AbstractUser):

    profil_photo = models.ImageField()
    role = models.CharField(
        max_length=30, 
        choices=RoleType.choices, 
        default=RoleType.CREATOR,
        verbose_name="Rôle")
