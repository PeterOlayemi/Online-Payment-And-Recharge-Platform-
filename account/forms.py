from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Myuser

class RegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=30, required=True, help_text='Enter Your First Name')
    last_name=forms.CharField(max_length=30, required=True, help_text='Enter Your Last Name')
    email=forms.EmailField(max_length=50, help_text='Enter A Valid Email Address')

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

class MyuserForm(forms.ModelForm):
    date_of_birth=forms.DateField(required=True, help_text='Enter Your Date of Birth in format (yyyy-mm-dd)')
    whatsapp_enabled_phone_number = forms.CharField(required=True, help_text='A WhatsApp Enabled Phone Number is Required')
    home_address = forms.CharField(required=True, help_text='Enter your Home Address')

    class Meta:
        model = Myuser
        fields=['date_of_birth','whatsapp_enabled_phone_number','home_address']
        labels={}