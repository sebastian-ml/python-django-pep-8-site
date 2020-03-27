from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='forum-main'),
    path('community/',
         views.CommunityTemplateView.as_view(),
         name='forum-community'
         ),
    path('featured/',
         views.FeaturedTemplateView.as_view(),
         name='forum-featured'),
    path('featured/subpage1/',
         views.FeaturedSubpage1TemplateView.as_view(),
         name='forum-featured-subpage1'),
]