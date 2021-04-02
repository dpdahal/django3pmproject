from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'pages/index/index.html')


def about(request):
    return render(request, 'pages/about/about.html')


def contact(request):
    return render(request, 'pages/contact/contact.html')
