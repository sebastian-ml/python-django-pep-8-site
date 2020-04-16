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
        context['first_subpage'] = 'Forum'
        return context


class FeaturedTemplateView(TemplateView):
    template_name = 'forum/featured.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Featured'
        context['first_subpage'] = 'Forum'
        return context


class FeaturedSubpage1TemplateView(TemplateView):
    template_name = 'forum/featured-subpage1.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Featured'
        context['subheading'] = 'Category1'
        context['first_subpage'] = 'Forum'
        context['second_subpage'] = 'Featured'
        return context


class FeaturedSubpage2TemplateView(FeaturedSubpage1TemplateView):
    template_name = 'forum/featured-subpage2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subheading'] = 'Category2'
        return context


class FeaturedSubpage3TemplateView(FeaturedSubpage1TemplateView):
    template_name = 'forum/featured-subpage3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subheading'] = 'Category3'
        return context


class FeaturedSubpage4TemplateView(FeaturedSubpage1TemplateView):
    template_name = 'forum/featured-subpage4.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subheading'] = 'Category4'
        return context


class FeaturedSubpage5TemplateView(FeaturedSubpage1TemplateView):
    template_name = 'forum/featured-subpage5.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subheading'] = 'Category5'
        return context


