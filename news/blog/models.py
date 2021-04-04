from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class SettingModel(models.Model):
    company_name = models.CharField(max_length=200)
    company_email = models.CharField(max_length=200)
    company_phone = models.CharField(max_length=100)
    company_address = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to='logo', null=True)
    company_fax = models.IntegerField(null=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'setting'


class Slider(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='slider')
    description = RichTextField()
    status = models.BooleanField(default=0)

    def __str__(self):
        return self.title
