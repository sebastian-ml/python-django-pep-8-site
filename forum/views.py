from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Section, Category, Topic, Post
from django.urls import reverse
from django.views.generic import (CreateView,
                                  ListView,
                                  DetailView,
                                  DeleteView,
                                  UpdateView)


class SectionListView(ListView):
    model = Section
    context_object_name = 'sections'
    ordering = ['name']


class SectionDetailView(DetailView):
    model = Section
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(
            section=self.object.pk
        )

        return context


class CategoryDetailView(DetailView):
    model = Category
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topics'] = Topic.objects.filter(
            category=self.object.pk
        )

        return context


class TopicCreateView(LoginRequiredMixin, CreateView):
    """Create new topic."""
    model = Topic
    fields = ['title', 'content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(
            id=self.kwargs.get('category_id')
        )

        return context

    def form_valid(self, form):
        """
        Fill the author and category automatically.
        """
        # Set logged user as author of the post
        form.instance.author = self.request.user
        form.instance.category = Category.objects.get(
            id=self.kwargs.get('category_id')
        )

        return super().form_valid(form)


class TopicDetailView(DetailView):
    model = Topic


class TopicUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Topic
    fields = ['title', 'content']

    def test_func(self):
        topic = self.get_object()

        return (self.request.user == topic.author
                or self.request.user.is_superuser)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = self.get_object()

        return context


class TopicDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Topic

    def test_func(self):
        topic = self.get_object()

        return (self.request.user == topic.author
                or self.request.user.is_superuser)

    def get_success_url(self):
        topic = self.get_object()
        return reverse('forum:category', kwargs={
            'section_name': topic.category.section.name,
            'name': topic.category.name
        })


class PostCreateView(CreateView):
    model = Post
    fields = ['content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = Topic.objects.get(id=self.kwargs.get('pk'))

        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.topic = Topic.objects.get(id=self.kwargs.get('pk'))

        return super().form_valid(form)
