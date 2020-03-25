from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import TemplateView, UpdateView

from .models import Profile


class ProfileView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'users/profile.html'


class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = Profile
    template_name = 'users/profile_update.html'
    fields = ['email', 'city', 'born', 'sex']
    success_message = 'Zaktualizowano profil'

    def get_object(self):
        return self.request.user.profile

    def get_success_url(self):
        return reverse('profile-update')