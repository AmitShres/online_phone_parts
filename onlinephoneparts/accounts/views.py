from accounts.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login, logout, user_logged_in
from django.contrib.auth.decorators import login_required


# Create your views here.

def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        customer = User.objects.filter(username = username).first()
        if customer is None:
            messages.success(request, 'User not found.')
            return redirect('/login')
        
        
        profile_obj = Profile.objects.filter(user = customer ).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/login')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/login')
        
        login(request , user)
        return redirect('/')

    return render(request , 'Account/login.html')

def register_attempt(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name =request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/register')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register')
            
            customer = User.objects.create_user(username,email,pass1)
            customer.first_name=first_name
            customer.last_name=last_name
            customer.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = customer , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('/token_send')

        except Exception as e:
            print(e)


    return render(request , 'Account/register.html')

def success(request):
    return render(request , 'Account/success.html')


def token_send(request):
    return render(request , 'Account/token_send.html')



def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/login')
        else:
            return redirect('/error.html')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'Accout/error.html')








def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )

def logout_attempt(request):
    logout(request)
    return render(request, 'Main/index.html')
    