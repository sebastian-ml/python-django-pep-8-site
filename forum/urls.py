from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('',
         views.SectionListView.as_view(
             template_name=f'{app_name}/main.html'),
         name='main'),
    path('<str:name>/',
         views.SectionDetailView.as_view(
             template_name=f'{app_name}/section.html'),
         name='section'),
    path('<str:section_name>/<str:name>/',
         views.CategoryDetailView.as_view(
             template_name=f'{app_name}/category.html'),
         name='category'),
    path('<str:section_name>/<int:category_id>/create-post/',
         views.TopicCreateView.as_view(
             template_name=f'{app_name}/topic_form.html'),
         name='topic-create'),
]
