from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextChoices, Model, DecimalField, PositiveIntegerField, \
    BooleanField, OneToOneField, CASCADE, ImageField, ForeignKey, TextField, DateTimeField

from apps.models.managers import CustomUserManager


class User(AbstractUser):
    class Role(TextChoices):
        WORKER = 'worker', 'WORKER'
        CUSTOMER = 'customer', 'CUSTOMER'
        ADMIN = 'admin', 'ADMIN'

    role = CharField(max_length=15, choices=Role.choices, default=Role.CUSTOMER)
    phone_number = CharField(unique=True, max_length=9)
    profile_image = ImageField(upload_to='users/%Y/%m/%d')
    objects = CustomUserManager()


class WorkerProfile(Model):
    bio = CharField(max_length=150)
    latitude = CharField(max_length=15)
    longitude = CharField(max_length=15)
    city = CharField(max_length=20)
    rating = DecimalField(max_digits=1, decimal_places=1)
    completed_orders_count = PositiveIntegerField(default=0)
    is_available = BooleanField(default=True)
    user = OneToOneField('apps.User', CASCADE, related_name='worker_profile')


class Portfolio(Model):
    worker = ForeignKey("apps.WorkerProfile", on_delete=CASCADE, related_name='portfolio')

    title = CharField(max_length=150)

    description = TextField()
    image = ImageField(upload_to='portfolio/%Y/%m/%d')

    created_at = DateTimeField(auto_now_add=True)
