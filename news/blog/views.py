import datetime

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from blog.froms import ContactFrom
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

from django.views import generic
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.utils import timezone


# Create your views here.

class StudentViews(generic.ListView):
    template_name = 'students/student.html'
    model = Student
    context_object_name = 'studentData'


class StudentAdd(generic.CreateView):
    template_name = 'students/add-student.html'
    model = Student
    fields = '__all__'


class StudentDelete(generic.DeleteView):
    template_name = 'students/delete-student.html'
    model = Student
    success_url = '/student'


class StudentEdit(generic.UpdateView):
    template_name = 'students/edit-student.html'
    model = Student
    success_url = '/student'
    fields = '__all__'


def index(request):
    data = {
        'sliderData': Slider.objects.all(),

    }
    return render(request, 'pages/index/index.html', data)


def about(request):
    data = {
        'aboutData': About.objects.first()
    }
    return render(request, 'pages/about/about.html', data)


def get_package(request):
    data = {
        'packageData': Package.objects.all()
    }
    return render(request, 'pages/package/package.html', data)


def package_details(request, id):
    data = {
        'packageDetails': Package.objects.get(id=id)
    }
    return render(request, 'pages/package/package-details.html', data)


@csrf_exempt
def contact(request):
    if request.method == "POST":
        fm = ContactFrom(request.POST)
        if fm.is_valid():
            fm.save()
            name = request.POST.get('full_name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            send_mail(subject, message, email, ['laravel3pm@gmail.com'])
            data = {
                'success': "Contact was successfully send",
                'status': 200
            }
            return JsonResponse(data)


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
    user_id = request.user.id
    data = {
        'bookingData': Booking.objects.filter(user_id=user_id).select_related('package_id')

    }
    return render(request, 'users/users.html', data)


def users_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')


def page_not_found(request, exception):
    return render(request, 'errors/404.html')


def book(request, package_id):
    if request.user.is_authenticated:
        uId = request.user.id
        user = User.objects.get(id=uId)
        package = Package.objects.get(id=package_id)
        obj = Booking.objects.create(
            booking_date=timezone.now(),
            package_id=package,
            user_id=user
        )
        obj.save()

        messages.success(request, 'Booking successfully created')
        return redirect('users')

    else:
        return redirect('login')
