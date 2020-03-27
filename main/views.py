from django.shortcuts import render


def home(request):
    return render(request, 'main/main.html')


def contact(request):
    context = {'heading': 'Contact'}
    return render(request, 'main/contact.html', context)


def about(request):
    context = {'heading': 'About'}
    return render(request, 'main/about.html', context)