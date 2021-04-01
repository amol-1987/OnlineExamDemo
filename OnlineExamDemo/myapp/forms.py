from django import forms
from myapp.models import *
from django.contrib.auth.models import User
class RForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','password','email')



class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username','password')
