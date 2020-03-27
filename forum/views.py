from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'forum/main.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Forum'
        return context


class CommunityTemplateView(TemplateView):
    template_name = 'forum/community.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Społeczność'
        context['first_previous_page'] = 'Forum'
        return context


class FeaturedTemplateView(TemplateView):
    template_name = 'forum/featured.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Featured'
        context['first_previous_page'] = 'Forum'
        return context


class FeaturedSubpage1TemplateView(TemplateView):
    template_name = 'forum/featured-subpage1.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Featured'
        context['subheading'] = 'Category1'
        context['first_previous_page'] = 'Featured'
        context['second_previous_page'] = 'Forum'
        return context
