from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        """Get an e-mail and check if it already exists in db."""

        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise ValidationError("Podany adres e-mail jest już wykorzystywany")
        return email

    class Meta:
        model = User
        fields = [
            'username', 'email',
            'password1', 'password2',
        ]
