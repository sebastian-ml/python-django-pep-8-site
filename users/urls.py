from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(
             redirect_authenticated_user=True,
             template_name=f'{app_name}/login.html'
         ),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(
             template_name=f'{app_name}/logout.html'
         ),
         name='logout'),
    path('register/',
         views.RegisterCreateView.as_view(
             template_name=f'{app_name}/register.html'
         ),
         name='register'),
    path('profile/',
         views.ProfileView.as_view(
             template_name=f'{app_name}/profile.html'
         ),
         name='profile'),
    path('profile/<int:pk>/',
         views.ProfileDetailView.as_view(
             template_name=f'{app_name}/profile_details.html'
         ),
         name='profile-details'),
    path('settings/',
         views.ProfileUpdateView.as_view(
             template_name=f'{app_name}/profile_update.html'
         ),
         name='profile-update'),
]
