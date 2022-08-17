from django.views.generic import TemplateView


class Handler404TemplateView(TemplateView):
    template_name = 'errors/404.html'
