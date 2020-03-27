from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='forum-main'),
    path('community/',
         views.CommunityTemplateView.as_view(),
         name='forum-community'
         ),
]