from django.shortcuts import render, redirect, render_to_response
from django.contrib import auth
from MCS.models import CustomUser
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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/accounts/login/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html',{'form': form})