from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    """Create profile. Link each profile with User. 1 Profile - 1 User"""
    MALE = 'M'
    FEMALE = 'F'
    UNDEFINED = 'U'
    SEX_TO_CHOICE = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNDEFINED, 'Undefined'),
    ]

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    email = models.EmailField(null=True,
                              blank=True,
                              unique=True)
    city = models.CharField(null=True,
                            blank=True,
                            default=None,
                            max_length=30)
    born = models.DateField(null=True,
                            blank=True,
                            default=None)
    sex = models.CharField(max_length=1,
                           choices=SEX_TO_CHOICE,
                           null=True,
                           blank=True,
                           default=None)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('users:profile-details', kwargs={'pk': self.pk})
