from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextChoices

from apps.models.managers import CustomUserManager


class User(AbstractUser):
    class Role(TextChoices):
        ADMIN = 'worker', 'WORKER'
        AUTHOR = 'customer', 'CUSTOMER'
        READER = 'admin', 'ADMIN'

    role = CharField(max_length=15, choices=Role.choices, default=Role.READER)

    objects = CustomUserManager()