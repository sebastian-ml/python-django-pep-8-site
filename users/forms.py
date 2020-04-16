from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):
    """Custom register form."""
    # Add additional field to form to store user email
    email = forms.EmailField()

    def clean_email(self):
        """Get an e-mail and check if it already exists in db."""
        email = self.cleaned_data['email']
        # If email already exists in db raise an error
        if User.objects.filter(email=email):
            raise ValidationError("Podany adres e-mail jest już wykorzystywany")
        return email

    class Meta:
        # Choose fields that are displayed during the registration process
        model = User
        fields = [
            'username', 'email',
            'password1', 'password2',
        ]
