from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request, 'forum/main.html')


class CommunityTemplateView(TemplateView):
    template_name = 'forum/community.html'
