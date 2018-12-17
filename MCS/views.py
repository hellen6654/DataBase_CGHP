# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect, render_to_response
from django.contrib import auth
from MCS.models import CustomUser, Member, Employee
from .forms import CustomUserCreationForm

"""
參考文件:
http://dokelung-blog.logdown.com/posts/234437-django-notes-10-users-login-and-logout
"""

def login(request):
    # 如果已經有用戶登入了, 跳轉至首頁
    if request.user.is_authenticated:
        return redirect('/index/')

    email = request.POST.get('email')
    password = request.POST.get('password')
    
    if email and password:
        try:
            user = auth.authenticate(email=email, password = password)
        except:
            return render(request, 'login.html')
        # 登入成功
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('/index/')
    return render(request, 'login.html')
'''
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/accounts/login/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html',{'form': form})
'''
def Create_Member_View(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            member = Member.create(user=user)
            member.save()
            auth.login(request, user)
            return redirect('/index/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'create-member.html',{'form': form})

def Create_Employee_View(request):
    title =  request.POST.get('title')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            employee = Employee.create(user=user, title=title)
            employee.save()
            auth.login(request, user)
            return redirect('/index/')
            #return redirect('/accounts/login/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'create-employee.html',{'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/index/')