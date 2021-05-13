from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('slider-details/<slug>', views.slider_details, name='slider-details'),
    path('blog/<cat_slug>', views.category_data, name='category_blog'),
    path('blog/blog_details/<slug>', views.blog_details, name='blog_details'),
    path('register', views.user_register, name='register'),
    path('login', views.user_login, name='login'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password-reset.html'),
         name='password-reset'),

    path('password_reset_confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password-reset-confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_done',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('users', views.users, name='users'),
    path('user_logout', views.users_logout, name='user_logout'),
    path('student', views.StudentViews.as_view(), name='student'),
    path('add-student', views.StudentAdd.as_view(), name='add-student'),
    path('student/delete-student/<pk>', views.StudentDelete.as_view(), name='delete-student'),
    path('student/edit-student/<pk>', views.StudentEdit.as_view(), name='edit-student'),

    path('package', views.get_package, name='package'),
    path('package/package-details/<id>', views.package_details, name='package-details'),

    path('booking/<package_id>', views.book, name='booking'),

    path('get_booking_details/<id>', views.get_booking_details, name='get_booking_details'),
    path('create-checkout-session/<id>', views.CreateCheckoutSession.as_view(), name='create-checkout-session'),
    path('success', views.SuccessPayment.as_view(), name='success'),
    path('cancel', views.CancelPayment.as_view(), name='cancel'),
    path('gallery', views.gallery, name='gallery'),

    path('employee', views.employee, name='employee'),
    path('employee-get', views.employee_get, name='employee-get'),
    path('employee-insert', views.employee_insert, name='employee-insert'),
    path('employee-delete/<id>', views.employee_delete, name='employee-delete'),
    path('employee-edit/<id>', views.employee_edit, name='employee-edit'),
    path('employee-update/<id>', views.employee_update, name='employee-update'),

]
