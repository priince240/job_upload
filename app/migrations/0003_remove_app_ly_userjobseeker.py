# Generated by Django 4.2.5 on 2023-09-19 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_app_ly_userjobseeker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app_ly',
            name='userjobseeker',
        ),
    ]