from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-page'),
    path('contact/', views.contact, name='contact-page'),
    path('about/', views.about, name='about-page'),
]