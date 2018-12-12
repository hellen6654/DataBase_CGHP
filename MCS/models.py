# -*- coding: UTF-8 -*-
from django.db import models
import uuid
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
#
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('id_TW', 'Y100000000')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    GENDER_FEMALE = 'F'
    GENDER_MALE = 'M'
    
    id_TW = models.CharField(
        verbose_name='在台灣的身分證號碼', max_length=10, null=False, unique=True,
        validators=[RegexValidator(r'^[A-Z]{1}[1-2]{1}[0-9]{8}$')])
    phone_number = models.CharField(
        verbose_name='使用者電話號碼', max_length=15, null=False, default='',
        validators=[RegexValidator(r'^[0-9+()-]+$')])
    address = models.CharField(
        verbose_name='使用者住址', max_length=80, null=False,default='')
    age = models.PositiveIntegerField(
        verbose_name='使用者年齡', blank=True,default=0)

    GENDER_IN_USER_CHOICES = ((GENDER_FEMALE, 'Female'), (GENDER_MALE, 'Male'),)

    gender = models.CharField(
        verbose_name='使用者性別', max_length=1, choices=GENDER_IN_USER_CHOICES, null=False, default=GENDER_MALE)

    discount = models.DecimalField(
        verbose_name='使用者折扣', max_digits=3, decimal_places=2, null=False, default=1.00,
        validators=[MinValueValidator(0, '0<=使用者折扣<=1'), MaxValueValidator(1, '0<=使用者折扣<=1')])
    #====================================================
    username = None
    email = models.EmailField(_('email address'), unique=True)
    last_name = models.CharField(verbose_name='姓', max_length=4, null=False, default='')
    first_name = models.CharField(verbose_name='名', max_length=8, null=False, default='')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

class Member(models.Model):
    # 指向 User 的 primary_key = User.user_id
    user_id = models.OneToOneField(
        CustomUser, verbose_name='會員的使用者編號', on_delete=models.CASCADE, null=False)

    member_id = models.UUIDField(
        verbose_name='會員編號', null=False, primary_key=True,
        default=uuid.uuid4, editable=False)

class Employee(models.Model):
    # 指向 User 的 primary_key = User.user_id
    user_id = models.OneToOneField(
        CustomUser, verbose_name='會員的使用者編號', on_delete=models.CASCADE, null=False)

    # admin分配的帳號, 用來登入
    employee_id = models.UUIDField(
        verbose_name='員工編號', null=False, primary_key=True,
        default=uuid.uuid4, editable=False)

    title = models.CharField(
        verbose_name='員工職稱', max_length=8, null=False)
'''
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
'''