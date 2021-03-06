# Generated by Django 3.2 on 2021-05-09 09:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210429_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='blognews',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 5, 9, 9, 57, 26, 808107, tzinfo=utc)),
        ),
    ]
