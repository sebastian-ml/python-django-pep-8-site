from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Allow user to create a post."""
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=500)
    author = models.ForeignKey(User,
                               on_delete=models.SET_DEFAULT,
                               default='deleted_user')
    date_posted = models.DateTimeField(default=timezone.now)
