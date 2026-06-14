from django.db.models import Model, CharField, ForeignKey, TextField, CASCADE, DateTimeField


class Region(Model):
    name = CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class District(Model):
    region = ForeignKey('apps.Region', on_delete=CASCADE, related_name='districts')
    name = CharField(max_length=50)

    def __str__(self):
        return f"{self.region.name} - {self.name}"


class JobPost(Model):
    user = ForeignKey('apps.User', on_delete=CASCADE, related_name='job_posts')
    title = CharField(max_length=200)
    description = TextField()
    section = ForeignKey('apps.Section', on_delete=CASCADE, related_name='job_posts')
    job = ForeignKey('apps.Job', on_delete=CASCADE, related_name='job_posts')
    region = ForeignKey('apps.Region', on_delete=CASCADE, related_name='job_posts')
    district = ForeignKey('apps.District', on_delete=CASCADE, related_name='job_posts')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} — {self.title}"