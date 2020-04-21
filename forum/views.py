from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView
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


class PostCreateView(LoginRequiredMixin, CreateView):
    """Create a post."""
    template_name = 'forum/post_create.html'
    # Variable to gather data from urls.py
    forum_id = None
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """
        Fill the author and forum_id automatically.
        User doesn't see these fields.
        """
        # Set logged user as author of the post
        form.instance.author = self.request.user
        # Get forum_id from parameter passed in urls.py
        form.instance.forum_id = self.forum_id

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Extend basic context by custom keys."""
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Dodaj nowy temat'
        context['first_subpage'] = 'Forum'
        context['second_subpage'] = 'Featured'

        return context


class PostListView(ListView):
    """Display all posts on a specific topic."""
    template_name = 'forum/forum_category.html'
    model = Post
    subheading = None
    forum_id = None

    def get_context_data(self, **kwargs):
        """Extend basic context by custom keys."""
        context = super().get_context_data(**kwargs)
        # First 3 context keys are the same for each featured subpage
        context['heading'] = 'Featured'
        context['first_subpage'] = 'Forum'
        context['second_subpage'] = 'Featured'
        # Get subheading from urls.py
        context['subheading'] = self.subheading
        # Get posts filtered by forum_id - forum_id indicated in urls.py
        context['posts'] = Post.objects.filter(forum_id=self.forum_id). \
            order_by('-date_posted')

        return context








