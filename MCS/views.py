# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect
from django.contrib import auth
from MCS.models import CustomUser, Member, Employee
from .forms import CustomUserCreationForm

"""
參考文件:
http://dokelung-blog.logdown.com/posts/234437-django-notes-10-users-login-and-logout
http://dokelung-blog.logdown.com/posts/235711-django-notes-12-template-advanced-technique
https://stackoverflow.com/questions/45122421/refer-to-admin-site-using-url-admin-in-app-django
"""

def login(request):
    email = request.POST.get('login-email')
    password = request.POST.get('login-password')

    login_message = ''
    
    if email and password:
        try:
            user = auth.authenticate(email=email, password = password)
        except:
            login_message = 'F'
        if user is not None and user.is_active:
            auth.login(request, user)
            login_message = 'S'
        else:
            login_message = 'F'
    return render(request, 'login.html', {'login_message': login_message})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            member = Member.create(user=user)
            member.save()
            auth.login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html',{'form': form})

def Create_Employee_View(request):
    title =  request.POST.get('register-title')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid() and title:
            user = form.save()
            member = Member.create(user=user)
            member.save()
            employee = Employee.create(user=user, title=title)
            employee.save()
            auth.login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register-employee.html',{'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/')