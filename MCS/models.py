# -*- coding: UTF-8 -*-
from django.db import models
import uuid
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
    GENDER_FEMALE = 'F'
    GENDER_MALE = 'M'

    # 系統自己生成一組不重複的亂數
    user_id = models.UUIDField(
    	verbose_name='使用者編號', null=False, primary_key=True,
    	default=uuid.uuid4, editable=False)

    # 身份證字號雖然具有唯一性, 但其為個人機密, 不應該隨意傳送, 容易造成資料外洩
    id_TW = models.CharField(
        verbose_name='在台灣的身分證號碼', max_length=10, null=False,
        validators=[RegexValidator(r'^[A-Z]{1}[1-2]{1}[0-9]{8}$')])
    password = models.CharField(
        verbose_name='使用者密碼', max_length=25, null=False)
    name = models.CharField(
        verbose_name='使用者姓名', max_length=20, null=False)
    phone_number = models.CharField(
        verbose_name='使用者電話號碼', max_length=15, null=False)
    address = models.TextField(
        verbose_name='使用者住址', null=False)
    age = models.PositiveIntegerField(
        verbose_name='使用者年齡')

    GENDER_IN_USER_CHOICES = ((GENDER_FEMALE, 'Female'), (GENDER_MALE, 'Male'),)

    gender = models.CharField(
        verbose_name='使用者性別', max_length=1, choices=GENDER_IN_USER_CHOICES, null=False)
    discount = models.DecimalField(
        verbose_name='使用者折扣', max_digits=2, decimal_places=2, null=False, 
        validators=[MinValueValidator(0, '0<=使用者折扣<=1'), MaxValueValidator(1, '0<=使用者折扣<=1')])
    def __str__(self):
        return self.name

class Member(models.Model):
	# 指向 User 的 primary_key = User.user_id
    user_id = models.OneToOneField(
        User, verbose_name='會員的使用者編號', on_delete=models.CASCADE, null=False)

    # 會員註冊時自訂的登入帳號
    member_id = models.CharField(
        verbose_name='會員編號', max_length=32, null=False, primary_key=True)

class Employee(models.Model):
	# 指向 User 的 primary_key = User.user_id
    user_id = models.OneToOneField(
        User, verbose_name='員工的使用者編號', on_delete=models.CASCADE, null=False)

    # admin分配的帳號, 用來登入
    employee_id = models.CharField(
        verbose_name='員工編號', max_length=32, null=False, primary_key=True)

    title = models.CharField(
        verbose_name='員工職稱', max_length=8, null=False)
