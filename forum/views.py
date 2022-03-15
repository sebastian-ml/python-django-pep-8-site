from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView
from .models import Section, Category, Topic


class SectionListView(ListView):
    model = Section
    context_object_name = 'sections'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Forum'
        context['breadcrumbs'] = True

        return context


class SectionDetailView(DetailView):
    model = Section
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = self.object.name
        context['breadcrumbs'] = True
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
        context['heading'] = self.object.name
        context['breadcrumbs'] = True
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
        context['heading'] = 'Add new topic'
        context['breadcrumbs'] = True

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = self.object.category.name
        context['breadcrumbs'] = True

        return context
