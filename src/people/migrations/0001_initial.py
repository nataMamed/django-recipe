# Generated by Django 3.0.7 on 2020-06-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=200)),
                ('person_email', models.CharField(max_length=200)),
            ],
        ),
    ]
