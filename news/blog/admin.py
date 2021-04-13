from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(SettingModel)
class AdminSetting(admin.ModelAdmin):
    list_display = ['company_name', 'company_email', 'company_phone']


@admin.register(Slider)
class AdminSlider(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_first', 'image']
    prepopulated_fields = {"slug": ("title",)}


@admin.register(BlogCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat_name']
    prepopulated_fields = {"slug": ("cat_name",)}


@admin.register(BlogNews)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'cat_id']
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'subject', 'message']
