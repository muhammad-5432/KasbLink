from django.db.models import Model, CharField, ForeignKey, PositiveIntegerField, CASCADE


class Section(Model):
    name = CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Job(Model):
    section = ForeignKey('apps.Section', on_delete=CASCADE, related_name='jobs')
    name = CharField(max_length=55)

    def __str__(self):
        return f"{self.section.name} — {self.name}"


class Service(Model):
    job = ForeignKey('apps.Job', on_delete=CASCADE, related_name='services')
    name = CharField(max_length=125)

    def __str__(self):
        return f"{self.job.name} — {self.name}"


class WorkerService(Model):
    worker = ForeignKey('apps.Worker', on_delete=CASCADE, related_name='worker_services')
    service = ForeignKey('apps.Service', on_delete=CASCADE, related_name='worker_services')
    price = PositiveIntegerField()

    class Meta:
        unique_together = ('worker', 'service')

    def __str__(self):
        return f"{self.worker.user.username} — {self.service.name} — {self.price}"
