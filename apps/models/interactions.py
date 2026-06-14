from django.db.models import (
    Model, TextField, DateTimeField, ForeignKey,
    PositiveSmallIntegerField, CASCADE
)
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(Model):
    user = ForeignKey('apps.User', on_delete=CASCADE, related_name='reviewers')
    worker = ForeignKey('apps.Worker', on_delete=CASCADE, related_name='reviews')
    rating = PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = TextField(null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'worker')

    def __str__(self):
        return f"{self.user.username} → {self.worker.user.username} — {self.rating}*"


class SavedWorker(Model):
    user = ForeignKey('apps.User', on_delete=CASCADE, related_name='saved_workers')
    worker = ForeignKey('apps.Worker', on_delete=CASCADE, related_name='saved_by')
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'worker')

    def __str__(self):
        return f"{self.user.username} → {self.worker.user.username}"