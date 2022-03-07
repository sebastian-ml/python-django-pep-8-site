from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Section, Category, Topic


class SectionListView(ListView):
    template_name = 'forum/main.html'
    model = Section
    context_object_name = 'sections'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Forum'

        return context


class SectionDetailView(DetailView):
    template_name = 'forum/section.html'
    model = Section
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = self.object.name
        context['categories'] = Category.objects.filter(
            section=self.object.pk
        )

        return context


class CategoryDetailView(DetailView):
    template_name = 'forum/category.html'
    model = Category
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = self.object.name
        context['topics'] = Topic.objects.filter(
            category=self.object.pk
        )

        return context


class TopicCreateView(LoginRequiredMixin, CreateView):
    """Create new topic."""
    template_name = 'forum/topic_form.html'
    model = Topic
    fields = ['title', 'content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Add new topic'

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
