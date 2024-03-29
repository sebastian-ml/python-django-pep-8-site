from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('',
         views.SectionListView.as_view(
             template_name=f'{app_name}/main.html'),
         name='main'),
    path('topic/<int:pk>/',
         views.TopicDetailView.as_view(
             template_name=f'{app_name}/topic_details.html'),
         name='topic-details'),
    path('topic/<int:pk>/update/',
         views.TopicUpdateView.as_view(
             template_name=f'{app_name}/topic_form.html'),
         name='topic-update'),
    path('topic/<int:pk>/delete/',
         views.TopicDeleteView.as_view(
             template_name=f'{app_name}/topic_delete_confirm.html'),
         name='topic-delete'),
    path('topic/<int:pk>/reply/',
         views.PostCreateView.as_view(
             template_name=f'{app_name}/post_form.html'),
         name='post-create'),
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
