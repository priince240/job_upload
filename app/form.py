from  django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
class sign_up(UserCreationForm):
    email=forms.EmailField(max_length=300)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
