# Generated by Django 4.2.5 on 2023-09-20 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_app_ly_job_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseekerprofile',
            name='expected_salary',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]