from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, CreateView

from .models import Profile
from .forms import UserRegisterForm


class ProfileView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'users/profile.html'


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Profile
    template_name = 'users/profile_update.html'
    fields = ['email', 'city', 'born', 'sex']
    success_message = 'Zaktualizowano profil'
    success_url = reverse_lazy('profile-update')

    def get_object(self):
        return self.request.user.profile


class RegisterCreateView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
