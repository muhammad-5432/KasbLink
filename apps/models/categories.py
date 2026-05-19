from django.db.models import Model, CharField, SlugField, PositiveIntegerField, TextField, ForeignKey, CASCADE


class Category(Model):
    name = CharField(unique=True, max_length=50)
    slug = SlugField(unique=True)


class Service(Model):
    name = CharField(max_length=50)
    min_price = PositiveIntegerField()
    max_price = PositiveIntegerField()
    worker = ForeignKey('apps.WorkerProfile', CASCADE, related_name='worker_services')
    category = ForeignKey('apps.Category', CASCADE, related_name='services')
