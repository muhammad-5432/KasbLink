from django.db.models import Model, CharField, SlugField, PositiveIntegerField, TextField, ForeignKey, CASCADE


class Category(Model):
    name = CharField(unique=True, max_length=50)
    icon = CharField(unique=True, max_length=25)
    slug = SlugField(unique=True)


class Service(Model):
    title = CharField(max_length=175)
    min_price = PositiveIntegerField()
    max_price = PositiveIntegerField()
    description = TextField()
    worker = ForeignKey('apps.WorkerProfile', CASCADE, related_name='services')
    category = ForeignKey('apps.Category', CASCADE, related_name='services')
