# Generated by Django 3.2 on 2021-04-21 10:31

import ckeditor.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210421_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='package')),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.AlterField(
            model_name='blognews',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 4, 21, 10, 31, 2, 721272, tzinfo=utc)),
        ),
    ]
