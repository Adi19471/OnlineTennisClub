
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.core import validators
from django import forms
from .models import Contact,OnlineBooking






class SignUpForm(UserCreationForm):
 password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 class Meta:
  model = User
  fields = ['username', 'first_name', 'last_name', 'email']
  labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
  widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
  'first_name':forms.TextInput(attrs={'class':'form-control'}),
  'last_name':forms.TextInput(attrs={'class':'form-control'}),
  'email':forms.EmailInput(attrs={'class':'form-control'}),
  }

class LoginForm(AuthenticationForm):
 username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
 password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))





class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = '__all__'
    
    

class OnlineBookingForm(forms.ModelForm):
  class Meta:
    model = OnlineBooking
    fields = '__all__'
    
    
class OnlineBookingForm(forms.ModelForm):
  
  class Meta:
    
   
    model = OnlineBooking
    fields = ['name', 'date', 'time','duration_of_game','number_of_player']
    labels = {'name': 'Enter Your Name', 'date': 'Select  Date', 'time': 'Enter Your Time','duration_of_game':'Duration Of Game Time','number_of_player':'Chose Number Of Player'}
   
    widgets = {
      'name': forms.TextInput(attrs={'class':'form-control'}),
      'date': forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
    

     'time': forms.TimeInput(attrs={'id':"timepicker",'class':'form-control',}),
      'duration_of_game': forms.NumberInput(attrs={'class':'form-control'}),
      'number_of_player': forms.NumberInput(attrs={'class':'form-control'}),
    
    
    }