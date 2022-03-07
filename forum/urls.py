from django.urls import path
from . import views
# dodac tu template name
app_name = 'forum'

urlpatterns = [
    path('',
         views.SectionListView.as_view(),
         name='main'),
    path('<str:name>/',
         views.SectionDetailView.as_view(),
         name='section'),
    path('<str:section_name>/<str:name>/',
         views.CategoryDetailView.as_view(),
         name='category'),
    path('<str:section_name>/<int:category_id>/create-post/',
         views.TopicCreateView.as_view(),
         name='topic-create'),
]
