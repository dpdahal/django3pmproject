from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(SettingModel)
class AdminSetting(admin.ModelAdmin):
    list_display = ['company_name', 'company_email', 'company_phone']


@admin.register(Slider)
class AdminSlider(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image']
    prepopulated_fields = {"slug": ("title",)}
