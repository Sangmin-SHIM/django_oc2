import imp
from django.db import models

class RoleType(models.TextChoices):
    CREATOR = "CREATOR", "Créateur"
    SUBSCRIBER = "SUBSCRIBER", "Abonné"