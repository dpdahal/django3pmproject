from django.shortcuts import render

from .models import *


# Create your views here.

def index(request):
    data = {
        'sliderData': Slider.objects.all()
    }
    return render(request, 'pages/index/index.html', data)


def about(request):
    return render(request, 'pages/about/about.html')


def contact(request):
    return render(request, 'pages/contact/contact.html')


def slider_details(request, slug):
    data = {
        'sliderData': Slider.objects.get(slug=slug)
    }
    return render(request, 'pages/slider/slider-details.html',data)
