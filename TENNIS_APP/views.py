import email
from multiprocessing import context
from time import time
from unicodedata import name
from django.shortcuts import render,redirect 

from django.shortcuts import render, HttpResponseRedirect
from .forms import OnlineBookingForm, SignUpForm, LoginForm,ContactForm,OnlineBookingForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import Group


from django.core.mail import send_mail
from django.conf import settings

from .models import Contact,OnlineBooking



# Create your views here.

def home_view(request):
 return render(request,"T-APP/home.html")



def about_view(request):
 return render(request,"T-APP/about.html")



def contact_view(request):
    if request.method == 'POST':
      fm = ContactForm(request.POST)
      if fm.is_valid():
        name = fm.cleaned_data['name']
        email = fm.cleaned_data['email']
        mobile_number = fm.cleaned_data['mobile_number']   
        address = fm.cleaned_data['address']
        user = Contact(name=name,email=email,mobile_number=mobile_number,address=address)
        user.save()
        fm = ContactForm()
    else:
     fm = ContactForm()
    return render(request, 'T-APP/contact.html',{'fm':fm})




def footer_view(request):
 return render(request, "T-APP/footer.html")



# Dashboard
def dashboard(request):
 if request.user.is_authenticated:
  # posts = Post.objects.all()
  user = request.user
  full_name = user.get_full_name()
  # gps = user.groups.all()
  return render(request, 'T-APP/dashboard.html')
 else:
  return HttpResponseRedirect('/home/')
 
 
 


# Logout
def user_logout(request):
 logout(request)
 return HttpResponseRedirect('/login/')

# Sigup
def user_signup(request):
 if request.method == "POST":
  form = SignUpForm(request.POST)
  if form.is_valid():
   messages.success(request, 'Congratulations!! You have become an Author.')
   user = form.save()
   group = Group.objects.get(name='Author')
   user.groups.add(group)
 else:
  form = SignUpForm()
 return render(request, 'T-APP/signup.html', {'form':form})

# Login
def user_login(request):
 if not request.user.is_authenticated:
  if request.method == "POST":
   form = LoginForm(request=request, data=request.POST)
   if form.is_valid():
    uname = form.cleaned_data['username']
    upass = form.cleaned_data['password']
    user = authenticate(username=uname, password=upass)
    if user is not None:
     login(request, user)
     messages.success(request, 'Logged in Successfully !!')
     return HttpResponseRedirect('/about/')
  else:
   form = LoginForm()
  return render(request, 'T-APP/login.html', {'form':form})
 else:
  return HttpResponseRedirect('/about/')








def email_view(request):
  if request.method == 'POST':
      subject = request.POST.get('subject')
      message = request.POST.get('message')
      email = request.POST.get('email')
      send_mail(subject, message, settings.EMAIL_HOST_USER,
                [email], fail_silently=False)
      return render(request, 'T-APP/email_sent.html', {'email': email})

  return render(request, 'T-APP/email.html', {})




def tennis_view(request):
  return render(request, 'T-APP/tennis.html')



def tennis_info_view(request):
  return render(request, 'T-APP/tennis_info_view.html')



def online_booking_view(request):
  if request.method == 'POST':
    fm = OnlineBookingForm(request.POST)
    if fm.is_valid():
      nm = fm.cleaned_data['name']
      em = fm.cleaned_data['date']
      ti = fm.cleaned_data['time']
      dg = fm.cleaned_data['duration_of_game']
      np = fm.cleaned_data['number_of_player']
      reg = OnlineBooking(name=nm,date=em,time=ti,duration_of_game=dg,number_of_player=np)
      reg.save()
      return redirect('/')
      fm = OnlineBookingForm()
      
  else:
    fm = OnlineBookingForm()
  return render(request, 'T-APP/online_booking.html',{'form':fm})



def display_booking_view(request):
  stud = OnlineBooking.objects.all()
 
  return render(request, 'T-APP/display_booking.html',{'stu':stud})

