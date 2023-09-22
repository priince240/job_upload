from django.contrib import admin
from django.urls import path
from .views import home,log__in,log_out,signup,profile_form,jobupload,appply,passwordchange,candidate_detail,delete,downloadresume,photo,display,update_profile,do_update_profile,jobupload_update,do_update_jobupload,profileview,viewprofile,reject,deleteexpirejobs
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name='home'),
    path("signup",signup,name='signup'),
    path("login",log__in,name='login'),
    path("logout",log_out,name='home'),
    path("profile",profile_form,name='profile'),
    path("update_profile/<int:id>",update_profile,name='update_profile'),
    path("do_update_profile/<int:id>",do_update_profile,name='do_update_profile'),
    path("profileview/<int:id>",profileview,name='profileviews'),
    path("viewprofile",viewprofile,name='viewprofile'),
    path("jobupload",jobupload,name='job upload'),
    path("jobupload_update/<int:id>",jobupload_update,name='job upload_update'),
    path("do_update_jobupload/<int:id>",do_update_jobupload,name='do_update_job upload'),
    path("apply/<int:id>",appply,name='apply'),
    path("passwordchange",passwordchange,name='passwordchange'),
    path("candidate_profile",candidate_detail,name='candidatedetail'),
    path("delete/<int:id>",delete,name='delete'),
    path("reject/<int:id>",reject,name='reject'),
    path("photo/<int:id>",photo,name='delete'),
    path("download-resume/<int:id>",downloadresume,name='downlaod-resume'),
    path("display",display,name='display'),
    path("candidate_detail",candidate_detail,name='candidate_-detail'),
    path("deletejobs",deleteexpirejobs,name='deletejobs'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
