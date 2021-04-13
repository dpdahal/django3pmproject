from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from blog.froms import ContactFrom
from django.core.mail import send_mail


# Create your views here.

def index(request):
    data = {
        'sliderData': Slider.objects.all()
    }
    return render(request, 'pages/index/index.html', data)


def about(request):
    return render(request, 'pages/about/about.html')


def contact(request):
    if request.method == "POST":
        obj = ContactFrom(request.POST)
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if obj.is_valid():
            obj.save()
            send_mail(subject, message, email, ['laravel3pm@gmail.com'])
            messages.success(request, 'Success')
            return redirect('contact')
        else:
            data = {
                'contactForm': obj
            }
            return render(request, 'pages/contact/contact.html', data)
    else:
        data = {
            'contactForm': ContactFrom()
        }
        return render(request, 'pages/contact/contact.html', data)


def slider_details(request, slug):
    data = {
        'sliderData': Slider.objects.get(slug=slug)
    }
    return render(request, 'pages/slider/slider-details.html', data)


def category_data(request, cat_slug):
    catData = BlogCategory.objects.get(slug=cat_slug)
    data = {
        'categoryData': catData,
        'blogData': BlogNews.objects.filter(cat_id=catData.id)
    }
    return render(request, 'pages/blog/blog-category.html', data)


def blog_details(request, slug):
    obj = BlogNews.objects.get(slug=slug)
    cat_name = obj.cat_id

    data = {
        'suggestNews': BlogNews.objects.filter(cat_id=cat_name),
        'blogDetails': BlogNews.objects.get(slug=slug)
    }
    return render(request, 'pages/blog/blog-details.html', data)


def user_register(request):
    if request.method == 'POST':
        user_obj = UserCreationForm(request.POST)
        if user_obj.is_valid():
            user_obj.save()
            messages.success(request, 'User was successfully created')
            return redirect('register')

        else:
            return redirect('register')
    else:
        data = {
            'userRegisterForm': UserCreationForm
        }
        return render(request, 'users/register.html', data)


def user_login(request):
    if request.method == "POST":
        user_request = AuthenticationForm(data=request.POST)
        if user_request.is_valid():
            user = user_request.get_user()
            login(request, user)
            return redirect('users')
        else:
            messages.error(request, 'Invalid Access')
            return redirect('login')

    else:
        data = {
            'loginForm': AuthenticationForm
        }
        return render(request, 'users/login.html', data)


@login_required(login_url='login')
def users(request):
    return render(request, 'users/users.html')


def users_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
