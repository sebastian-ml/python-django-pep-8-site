from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Section(models.Model):
    """Create new section in forum."""
    created_by = models.ForeignKey(User,
                                   on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    date_created = models.DateTimeField(default=timezone.now)


class Category(models.Model):
    """Create new category in certain forum section."""
    section = models.ForeignKey(Section,
                                on_delete=models.CASCADE,
                                related_name='categories')
    created_by = models.ForeignKey(User,
                                   on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    date_created = models.DateTimeField(default=timezone.now)


class Topic(models.Model):
    """Create new topic in certain category."""
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    author = models.ForeignKey(User,
                               on_delete=models.SET_DEFAULT,
                               default='Deleted account')
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('forum:topic-details', kwargs={'pk': self.pk})


class Post(models.Model):
    """Allow user to create a post."""
    topic = models.ForeignKey(Topic,
                              on_delete=models.CASCADE)
    author = models.ForeignKey(User,
                               on_delete=models.SET_DEFAULT,
                               default='Deleted account')
    content = models.TextField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)
