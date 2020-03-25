from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    UNDEFINED = 'U'
    SEX_TO_CHOICE = [
        (MALE, 'Mężczyzna'),
        (FEMALE, 'Kobieta'),
        (UNDEFINED, 'Nieokreślono'),
    ]

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE
                                )
    email = models.EmailField(verbose_name='Adres e-mail',
                              null=True,
                              blank=True,
                              unique=True
                              )
    city = models.CharField(verbose_name='Miejscowość',
                            null=True,
                            blank=True,
                            default=None,
                            max_length=30
                            )
    born = models.DateField(verbose_name='Urodziny',
                            null=True,
                            blank=True,
                            default=None
                            )
    sex = models.CharField(verbose_name='Płeć',
                           max_length=1,
                           choices=SEX_TO_CHOICE,
                           default=UNDEFINED
                           )

    def __str__(self):
        return self.user.username
