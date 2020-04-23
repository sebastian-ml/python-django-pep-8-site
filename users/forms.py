from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    """Custom register form."""
    # Add additional field to store user email
    email = forms.EmailField(required=True,
                             help_text="Required.")
    email2 = forms.EmailField(required=True,
                              help_text="Enter the same email as before, "
                                        "for verification.",
                              label='Email confirmation')

    def clean(self):
        """Clear emails, compare. Lower user input."""
        cleaned_data = super().clean()
        email = cleaned_data['email'].lower()
        email2 = cleaned_data['email2'].lower()

        # Check if both emails are the same
        if email and email2 and email != email2:
            self._errors['email2'] = self.error_class(
                ['Podane e-maile się różnią']
            )
            del self.cleaned_data['email2']

        # Check if email already exists in db
        if User.objects.filter(email=email):
            self._errors['email'] = self.error_class(
                ['Podany adres e-mail jest już wykorzystywany']
            )
            del self.cleaned_data['email']

        return cleaned_data

    class Meta:
        # Choose additional fields and set the order
        model = User
        fields = [
            'username', 'email',
            'email2', 'password1',
            'password2',
        ]

