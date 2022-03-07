from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, CreateView
from .models import Profile
from .forms import UserRegisterForm


class ProfileView(LoginRequiredMixin, TemplateView):
    """Show user profile."""
    model = User


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Allow user to update its profile and change some information."""
    model = Profile
    fields = ['email', 'city', 'born', 'sex']
    # Display a message when user updates its profile
    success_message = 'Zaktualizowano profil'
    success_url = reverse_lazy('users:profile-update')

    def get_object(self):
        """Get the id of logged user."""
        return self.request.user.profile


class RegisterCreateView(CreateView):
    """View responsible for user creation."""
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
