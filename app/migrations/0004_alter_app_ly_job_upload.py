# Generated by Django 4.2.5 on 2023-09-20 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_app_ly_userjobseeker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_ly',
            name='job_upload',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.employer'),
        ),
    ]