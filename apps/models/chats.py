from django.db.models import Model, ForeignKey, CASCADE, DateTimeField, BooleanField, TextField


class Conversation(Model):
    client = ForeignKey("apps.User", CASCADE, related_name="conversations")

    worker = ForeignKey("apps.WorkerProfile", CASCADE, related_name="conversations")

    created_at = DateTimeField(auto_now_add=True)


class Message(Model):
    conversation = ForeignKey(Conversation, CASCADE, related_name="messages")

    sender = ForeignKey("apps.User", CASCADE, related_name="messages")

    message = TextField()

    is_read = BooleanField(default=False)

    created_at = DateTimeField(auto_now_add=True)
