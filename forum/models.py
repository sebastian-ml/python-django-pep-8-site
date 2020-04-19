from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Allow user to create a post."""
    class Forums(models.IntegerChoices):
        """List of all pages with their id where user can create a post."""
        FEATURED_SUB1 = 11
        FEATURED_SUB2 = 12
        FEATURED_SUB3 = 13
        FEATURED_SUB4 = 14
        FEATURED_SUB5 = 15

    title = models.CharField(max_length=40)
    forum_id = models.IntegerField(choices=Forums.choices)
    content = models.TextField(max_length=500)
    author = models.ForeignKey(User,
                               on_delete=models.SET_DEFAULT,
                               default='deleted_user')
    date_posted = models.DateTimeField(default=timezone.now)
