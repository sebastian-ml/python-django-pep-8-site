from django.urls import path
from . import views


urlpatterns = [
    path('',
         views.HomeTemplateView.as_view(),
         name='forum-main'),
    path('community/',
         views.CommunityTemplateView.as_view(),
         name='forum-community'),
    path('featured/',
         views.FeaturedTemplateView.as_view(),
         name='forum-featured'),
    path('featured/subpage1/',
         views.FeaturedSubpage1TemplateView.as_view(),
         name='forum-featured-subpage1'),
    path('featured/subpage2/',
         views.FeaturedSubpage2TemplateView.as_view(),
         name='forum-featured-subpage2'),
    path('featured/subpage3/',
         views.FeaturedSubpage3TemplateView.as_view(),
         name='forum-featured-subpage3'),
    path('featured/subpage4/',
         views.FeaturedSubpage4TemplateView.as_view(),
         name='forum-featured-subpage4'),
    path('featured/subpage5/',
         views.FeaturedSubpage5TemplateView.as_view(),
         name='forum-featured-subpage5'),
]