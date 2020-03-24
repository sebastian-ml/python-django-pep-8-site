from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import TemplateView


class ProfileView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'users/profile_details.html'