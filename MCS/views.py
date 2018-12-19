# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect
from django.contrib import auth
from MCS.models import CustomUser, Member, Employee
from .forms import CustomUserCreationForm

"""
參考文件:
http://dokelung-blog.logdown.com/posts/234437-django-notes-10-users-login-and-logout
http://dokelung-blog.logdown.com/posts/235711-django-notes-12-template-advanced-technique
"""

def login(request):
    '''
    # 如果已經有用戶登入了, 跳轉至首頁
    if request.user.is_authenticated:
        return redirect('/index/')
    '''
    email = request.POST.get('login-email')
    password = request.POST.get('login-password')
    
    if email and password:
        try:
            user = auth.authenticate(email=email, password = password)
        except:
            # 回傳訊息
            return "帳號密碼有誤"
            #return render(request, 'login.html')
        # 登入成功
        if user is not None and user.is_active:
            auth.login(request, user)
            return "登入成功"
    else: "有欄位沒有填"
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
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            member = Member.create(user=user)
            member.save()
            auth.login(request, user)
            return '註冊成功'
    else:
        form = CustomUserCreationForm()
    return form

def Create_Member_View(request):
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
    return render(request, 'index.html',{'form': form})

def Create_Employee_View(request):
    title =  request.POST.get('title')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            employee = Employee.create(user=user, title=title)
            employee.save()
            auth.login(request, user)
            return render(request,'index.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'create-employee.html',{'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/')

# main home
def MCS_View(request, web):
    login_message = ''
    if 'login' in request.POST:
        login_message = login(request)

    register_message = register(request)
    if register_message == '註冊成功':
        return redirect('/')
    return render(request, web,{'form': register_message})