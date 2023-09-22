from django.db import models
from datetime import datetime,timedelta
from django.utils import timezone

# Create your models here.
# job seeker profile-------------------
class JobSeekerprofile(models.Model):
    name=models.CharField(max_length=220)
    age=models.CharField(max_length=100)
    profile=models.CharField(max_length=50)
    gender=models.CharField(max_length=100,choices=[('male','Male'),('female','Female'),('transgender','Transgender')])
    resume_upload=models.FileField(upload_to="resume/")
    photo=models.FileField(upload_to="photo/")
    resume_headline=models.TextField()
    keyskills=models.TextField()
    education=models.TextField()
    employment=models.CharField(max_length=100,choices=[('student','student'),('employed','employed'),('unemployed','unemployed'),('self employed','self employed')])
    project=models.TextField(null=True)
    project_summary=models.TextField(null=True)
    desired_jobtype=models.CharField(max_length=100,choices=[('full-time','full-time'),('part-time','part-time'),('internship','internship')])
    preferred_shift=models.CharField(max_length=100,choices=[('day-shift','day-shift'),('night-shift','night-shift'),('hybrid','hybrid'),('remote','remote')])
    expected_salary=models.CharField(max_length=1000,null=True)
    dob=models.DateTimeField(default=timezone.now , blank=True)
    email=models.EmailField(max_length=350)
    
    def __str__(self):
        return self.name
    
    
    
class employer(models.Model):
    jobtitle=models.CharField(max_length=200) 
    company=models.CharField(max_length=200)   
    salary=models.CharField(max_length=200) 
    experience_year=models.CharField(max_length=200)
    posted=models.DateTimeField(default=timezone.now , blank=True)
    openings=models.CharField(max_length=200)
    jobhighlights=models.TextField()
    application_deadline=models.CharField(max_length=150)
    location=models.CharField(max_length=220)  
    def __str__(self):
        return self.company
    
class app_ly(models.Model):
    job_upload=models.ForeignKey('employer',on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=350)
    resume=models.FileField(upload_to="resumeupload/",blank=False)
    candidate_photo=models.FileField(upload_to="photos/",blank=False)
    def __str__(self):
        return self.name
    
