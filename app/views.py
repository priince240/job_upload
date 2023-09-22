from django.shortcuts import render,HttpResponseRedirect,HttpResponse,redirect
from .form import sign_up
from datetime import datetime
from .models import JobSeekerprofile,app_ly,employer
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm
from django.contrib import messages
from django.core.mail import send_mail,send_mass_mail
from django.conf import settings
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        data=employer.objects.all()
        return render(request,"home.html",{'data':data})    
    return HttpResponseRedirect("/login")
def signup(request):
    
    if request.method == "POST":
        data=sign_up(data=request.POST)
        if data.is_valid():
            data.save()
            subject="welcome to fastjob"
            message='hi {data.cleaned_data["username"]},thankyou for registering in fastjob'
            email_from=settings.EMAIL_HOST_USER
            to=[data.cleaned_data["email"]]
            send_mail(subject,message,email_from,to)
            messages.success(request,"signup successfully----------")
            return HttpResponseRedirect("/signup")
    data=sign_up()
    return render(request,"signup.html",{'data':data})    
                
def log__in(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            data=AuthenticationForm(request=request,data=request.POST)
            if data.is_valid():
                username=data.cleaned_data["username"]
                password=data.cleaned_data["password"]
                user = authenticate (username=username , password=password )
                if user is not None:
                    login(request,user)
                    
                    messages.success(request,"login sucessfully----")
                return HttpResponseRedirect("/")
        else:
            data=AuthenticationForm()    
        return render(request,"login.html",{'data':data})
    else:
        return HttpResponse("you are login there is no need to login again---- go back")

def passwordchange(request):
    if  request.user.is_authenticated:
        if request.method=="POST":
            data=SetPasswordForm(user=request.user,data=request.POST)
            if data.is_valid():
                data.save()
            return HttpResponseRedirect("/login")
        data=SetPasswordForm(user=request.user)
        return render(request,"passwordchange.html",{'data':data})    
    else:
        return HttpResponseRedirect('/login')

def log_out(request):
    logout(request)
    return HttpResponseRedirect("/login")

def profile_form(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            name=request.POST.get('name')
            age=request.POST.get('age')
            profile=request.POST.get('profile')
            gender=request.POST.get('gender')
            resume_upload=request.FILES.get('resume_upload')
            photo=request.FILES.get("photo")
            resume_headline=request.POST.get('resume_headline')
            keyskills=request.POST.get('keyskills')
            education=request.POST.get('education')
            employment=request.POST.get('employment')
            project=request.POST.get('project')
            project_summary=request.POST.get('project_summary')
            desired_jobtype=request.POST.get('desired_jobtype')
            preferred_shift=request.POST.get('preferred_shift')
            expected_salary=request.POST.get('expected_salary')
            data=JobSeekerprofile(name=name,age=age,profile=profile,gender=gender,resume_upload=resume_upload,photo=photo,resume_headline=resume_headline,keyskills=keyskills,education=education,employment=employment,project=project,project_summary=project_summary,desired_jobtype=desired_jobtype,preferred_shift=preferred_shift,expected_salary=expected_salary,dob=datetime.now())
            data.save()

        return render(request,'profile.html')
    return HttpResponseRedirect("/login")

def update_profile(request,id):
    data=JobSeekerprofile.objects.get(id=id)
    return render(request,"update_profile.html",{'data':data})

def do_update_profile(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
                name=request.POST.get('name')
                age=request.POST.get('age')
                profile=request.POST.get('profile')
                gender=request.POST.get('gender')
                resume_upload=request.FILES.get('resume_upload')
                photo=request.FILES.get("photo")
                resume_headline=request.POST.get('resume_headline')
                keyskills=request.POST.get('keyskills')
                education=request.POST.get('education')
                employment=request.POST.get('employment')
                project=request.POST.get('project')
                project_summary=request.POST.get('project_summary')
                desired_jobtype=request.POST.get('desired_jobtype')
                preferred_shift=request.POST.get('preferred_shift')
                expected_salary=request.POST.get('expected_salary')
                data=JobSeekerprofile.objects.get(id=id)
                data.name=name
                data.age=age
                data.profile=profile
                data.gender=gender
                if resume_upload:
                    data.resume_upload=resume_upload
                data.resume_headline=resume_headline
                if photo:
                    data.photo=photo
                data.keyskills=keyskills
                data.education=education
                data.employment=employment
                data.project=project
                data.project_summary=project_summary
                data.desired_jobtype=desired_jobtype
                data.preferred_shift=preferred_shift
                data.expected_salary=expected_salary
                data.save()
                return redirect("/")
            




def jobupload(request):
    if request.user.is_staff:
        if request.method=="POST":
            jobtitle=request.POST.get("jobtitle")
            company=request.POST.get("company")
            salary=request.POST.get("salary")
            experience_year=request.POST.get("experience_year")
            openings=request.POST.get("openings")
            jobhighlights=request.POST.get("jobhighlights")
            application_deadline=request.POST.get("application_deadline")
            location=request.POST.get("location")
            data=employer(jobtitle=jobtitle,company=company,salary=salary,experience_year=experience_year,posted=datetime.now(),openings=openings,jobhighlights=jobhighlights,application_deadline=application_deadline,location=location)
            data.save()
            subject="job alert"
            message='hi {user.username},new jobs, come and check fastjob'
            email_from=settings.EMAIL_HOST_USER
            tos=[user.email for user in User.objects.all()]
            email_all=[(subject, message, email_from,[to])for to in tos]
            send_mass_mail(
                    email_all, fail_silently=False,
                )                   
        return render(request,"jobupload.html")
    return HttpResponse("you are not staff or employee so, go back")

def jobupload_update(request,id):
    if request.user.is_staff:
        data=employer.objects.get(id=id)
        return render(request,"jobupload_update.html",{'data':data})

def do_update_jobupload(request,id):
    if request.user.is_staff:
        data=employer.objects.get(id=id)
        if request.method=="POST":
            jobtitle=request.POST.get("jobtitle")
            company=request.POST.get("company")
            salary=request.POST.get("salary")
            experience_year=request.POST.get("experience_year")
            openings=request.POST.get("openings")
            jobhighlights=request.POST.get("jobhighlights")
            data.jobtitle=jobtitle
            data.company=company
            data.salary=salary
            data.expeirence_year=experience_year
            data.openings=openings
            data.jobhighlights=jobhighlights
            data.save()
            return redirect("/")

def reject(request,id):
    if request.user.is_staff:
        data = JobSeekerprofile.objects.get(id=id)
        subject="welcome to fastjob"
        message=f'hi {data.name},your application is not select thankyou better luck next time'
        email_from=settings.EMAIL_HOST_USER
        to=[data.email]
        send_mail(subject,message,email_from,to)
        data.delete()
        return redirect("/viewprofile")
    return HttpResponse("you are not staff and employee so, you cannot delete and application")

def delete(request,id):
    if request.user.is_staff:
        data=employer.objects.get(id=id)
        data.delete()
        return redirect("/")
    return HttpResponse("you are not staff or employee")

def appply(request,id):
    if request.user.is_authenticated:
        data1=employer.objects.get(id=id)
        if request.method=="POST":
            name=request.POST.get("name")
            email=request.POST.get("email")
            resume=request.FILES.get("resume")
            candidate_photo=request.FILES.get("candidate_photos")
          
            data=app_ly(name=name,email=email,resume=resume,candidate_photo=candidate_photo)
            data.save()
            subject="welcome to fastjob"
            message=f'hi {data.name},thankyou for applying in fastjob'
            email_from=settings.EMAIL_HOST_USER
            to=[data.email]
            send_mail(subject,message,email_from,to)
            messages.success(request,"applied successfully")
            return redirect("/display")
        return render(request,'apply.html',{'data1':data1})
    return HttpResponseRedirect("/login")
    
def candidate_detail(request):
    if request.user.is_staff:
        data=app_ly.objects.all()
        return render(request,"candidate_detail.html",{'data':data})
    return HttpResponse("you are not employee or staff so ,go back")
    
def downloadresume(request,id):
    data=JobSeekerprofile.objects.get(id=id)
    response=HttpResponse(data.resume_upload,content_type="application/force-download")
    response['Content-Disposition']=f'attachment:filename="{data.resume_upload.name}"'
    return response

def photo(request,id):
    data=JobSeekerprofile.objects.get(id=id)
    response=HttpResponse(data.photo,content_type="application/force-download")
    response['Content-Disposition']=f'attachment:filename="{data.photo.name}"'
    return response
def display(request):
    return render(request,"display.html ")

def profileview(request,id):
    data=JobSeekerprofile.objects.get(id=id)
    return render(request,"profileview.html",{'data':data})
def viewprofile(request):
    if request.user.is_staff:
        data=JobSeekerprofile.objects.all()
        return render(request,"viewprofile.html",{'data':data})
    return HttpResponse("you are not staff or employee")

def deleteexpirejobs(request):
    if request.user.is_staff:
        data=employer.objects.all()
        return render(request,"deleteexpirejobs.html",{'data':data})
    return HttpResponse("you are not staff or employee")