# Generated by Django 3.0.7 on 2020-06-26 00:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('ingredients', models.TextField()),
                ('preparation_method', models.TextField()),
                ('preparation_time', models.IntegerField()),
                ('revenue', models.CharField(max_length=50)),
                ('published', models.BooleanField(default=False)),
                ('registration_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]