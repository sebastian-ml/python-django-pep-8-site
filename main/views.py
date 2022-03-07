from django.shortcuts import render


def home(request):
    """Display main page."""
    return render(request, 'main/main.html')


def contact(request):
    """Display contact page. Set the heading also."""
    context = {'heading': 'Contact', 'breadcrumbs': True}
    return render(request, 'main/contact.html', context)


def about(request):
    """Display about page. Set the heading also."""
    context = {'heading': 'About', 'breadcrumbs': True}
    return render(request, 'main/about.html', context)
