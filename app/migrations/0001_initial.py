# Generated by Django 4.2.5 on 2023-09-19 12:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('salary', models.CharField(max_length=200)),
                ('experience_year', models.CharField(max_length=200)),
                ('posted', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('openings', models.CharField(max_length=200)),
                ('jobhighlights', models.TextField()),
                ('application_deadline', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='JobSeekerprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('age', models.CharField(max_length=100)),
                ('profile', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('transgender', 'Transgender')], max_length=100)),
                ('resume_upload', models.FileField(upload_to='resume/')),
                ('photo', models.FileField(upload_to='photo/')),
                ('resume_headline', models.TextField()),
                ('keyskills', models.TextField()),
                ('education', models.TextField()),
                ('employment', models.CharField(choices=[('student', 'student'), ('employed', 'employed'), ('unemployed', 'unemployed'), ('self employed', 'self employed')], max_length=100)),
                ('project', models.TextField(null=True)),
                ('project_summary', models.TextField(null=True)),
                ('desired_jobtype', models.CharField(choices=[('full-time', 'full-time'), ('part-time', 'part-time'), ('internship', 'internship')], max_length=100)),
                ('preferred_shift', models.CharField(choices=[('day-shift', 'day-shift'), ('night-shift', 'night-shift'), ('hybrid', 'hybrid'), ('remote', 'remote')], max_length=100)),
                ('expected_salary', models.CharField(max_length=255)),
                ('dob', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='app_ly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('resume', models.FileField(upload_to='resumeupload/')),
                ('candidate_photo', models.FileField(upload_to='photos/')),
                ('job_upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employer')),
            ],
        ),
    ]
