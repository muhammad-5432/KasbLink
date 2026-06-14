from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CharField, EmailField, ImageField, TextField, DecimalField, BooleanField,
    PositiveIntegerField, OneToOneField, ForeignKey,
    DateTimeField, TextChoices, Model, CASCADE, SET_NULL
)

from apps.models.managers import CustomUserManager


class User(AbstractUser):
    class Role(TextChoices):
        WORKER = 'worker', 'Worker'
        CUSTOMER = 'customer', 'Customer'
        ADMIN = 'admin', 'Admin'

    username = CharField(max_length=50, unique=True)
    email = EmailField(unique=True)
    first_name = CharField(max_length=50, null=True, blank=True)
    last_name = CharField(max_length=50, null=True, blank=True)
    phone = CharField(max_length=15, null=True, blank=True, unique=True)

    region = ForeignKey('apps.Region', SET_NULL, null=True, blank=True, related_name='users')
    district = ForeignKey(
        'apps.District',
        on_delete=SET_NULL,
        null=True, blank=True,
        related_name='users'
    )

    profile_image = ImageField(upload_to='profile_images/%Y/%m/%d', null=True, blank=True)
    role = CharField(max_length=15, choices=Role.choices, null=True, blank=True, default=None)
    created_at = DateTimeField(auto_now_add=True)
    is_onboarded = BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Worker(Model):
    class ExperienceYears(TextChoices):
        ONE_TO_THREE = '1-3', '1–3 yil'
        THREE_TO_FIVE = '3-5', '3–5 yil'
        FIVE_TO_TEN = '5-10', '5–10 yil'
        TEN_PLUS = '10+', '10+ yil'

    user = OneToOneField('apps.User', on_delete=CASCADE, related_name='worker')
    bio = TextField(max_length=750, null=True, blank=True)
    experience_years = CharField(max_length=10, choices=ExperienceYears.choices, null=True, blank=True)
    avg_rating = DecimalField(max_digits=3, decimal_places=1, default=0)
    is_available = BooleanField(default=True)
    review_count = PositiveIntegerField(default=0)
    last_online = DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class PortfolioMedia(Model):
    worker = ForeignKey('apps.Worker', on_delete=CASCADE, related_name='portfolio_media')
    file_url = ImageField(upload_to='portfolio_media/%Y/%m/%d', null=True, blank=True)
