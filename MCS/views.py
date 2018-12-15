from django.shortcuts import render, redirect, render_to_response
from django.contrib import auth
from django.contrib.auth.hashers import check_password
from MCS.models import CustomUser
#from .forms import CustomUserCreationForm
#from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm


def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    if email and password:
        try:
            user = auth.authenticate(email=email, password = password)
        except:
            print('error! except!')
            return render(request, 'login.html')
        if user is not None and user.is_active:
            print("yes")
            return redirect('/index/')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        print('post')
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print('save')
            user = form.save()
            return redirect('/accounts/login/')
    else:
        print('else')
        form = CustomUserCreationForm()
    print('return')
    return render(request, 'register.html',{'form': form})