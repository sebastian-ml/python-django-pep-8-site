from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Post


def forum_home(request):
    context = {'heading': 'Forum'}

    return render(request, 'forum/main.html', context)


def forum_community(request):
    context = {
        'heading': 'Społeczność',
        'first_subpage': 'Forum',
    }

    return render(request, 'forum/community.html', context)


def forum_featured(request):
    context = {
        'heading': 'Featured',
        'first_subpage': 'Forum',
    }

    return render(request, 'forum/featured.html', context)


class FeaturedSubpageView(TemplateView):
    subheading = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom context keys
        # First 3 context keys are the same for each featured subpage
        context['heading'] = 'Featured'
        context['first_subpage'] = 'Forum'
        context['second_subpage'] = 'Featured'
        # Subheading is different for each featured subpage
        context['subheading'] = self.subheading

        return context


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'forum/post_create.html'
    fields = ['title', 'content']



