# -*- coding: UTF-8 -*-
from django.db import models
import django.utils.timezone as timezone
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
        verbose_name='會員帳號', max_length=32, null=False, primary_key=True)

class Employee(models.Model):
	# 指向 User 的 primary_key = User.user_id
    user_id = models.OneToOneField(
        User, verbose_name='員工的使用者編號', on_delete=models.CASCADE, null=False)

    # admin分配的帳號, 用來登入
    employee_id = models.CharField(
        verbose_name='員工帳號', max_length=32, null=False, primary_key=True)

    title = models.CharField(
        verbose_name='員工職稱', max_length=8, null=False)

class Pizza(models.Model):
    pizza_no = models.AutoField(
        verbose_name='披薩編號', primary_key=True, null=False)
    name = models.CharField(
        verbose_name='披薩名稱', max_length=20, null=False)
    description = models.TextField(
        verbose_name='披薩描述')
    price = models.PositiveIntegerField(
        verbose_name='披薩價格', null=False)
    size = models.CharField(
        verbose_name='披薩尺寸', max_length=2, null=False)
    cost = models.PositiveIntegerField(
        verbose_name='披薩成本', null=False)
    in_stock = models.PositiveIntegerField(
        verbose_name='披薩庫存量', null=False)
    sales_volume = models.PositiveIntegerField(
        verbose_name='披薩銷售量', null=False, default=0) 
    click_count = models.PositiveIntegerField(
        verbose_name='披薩點擊量', null=False, default=0)    
    isVegetarian = models.BooleanField(
        verbose_name='是否為素食披薩', null=False)
    # 1 <= stars <= 5
    stars = models.DecimalField(
        verbose_name='披薩評分', max_digits=1, decimal_places=0, null=False,  
        validators=[MinValueValidator(1, '最低1分'), MaxValueValidator(5, '最多5分')]) #小數
    def __str__(self):
        return self.name
        
class Order(models.Model):
    order_no = models.AutoField(
    	verbose_name='訂單編號', null=False, primary_key=True)

    # 哪一個 會員 產生的訂單
    member_id = models.ForeignKey(
        Member, verbose_name='會員身分證號碼', on_delete=models.CASCADE, null=False)
    total_price = models.PositiveIntegerField(
    	verbose_name='訂單總價', null=False)
    ordered_date = models.DateTimeField(
    	verbose_name='訂單產生時間', default=timezone.now, null=False)

    # 若為 null 代表 尚未出貨
    shipped_date = models.DateTimeField(
    	verbose_name='實際出貨時間', default=timezone.now)
    discount = models.DecimalField(
        verbose_name='訂單折扣', max_digits=2, decimal_places=2, null=False, 
        validators=[MinValueValidator(0, '0 <= 訂單折扣 <= 1'), MaxValueValidator(1, '0 <= 訂單折扣 <= 1')])    

    # 訂單內容: 裡面有從購物車送出的字串資訊
    details = models.TextField(null=False)

    # 訂單狀態
    def GetState():
    	if shipped_date!=null : return "已出貨"
    	return "訂單處理中"

class Rate(models.Model):
    member_id = models.ForeignKey(
        Member, verbose_name='會員帳號', on_delete=models.CASCADE, null=False)

    pizza_no = models.ForeignKey(
        Pizza, verbose_name='披薩編號', on_delete=models.CASCADE, null=False)

    stars = models.DecimalField(
        verbose_name='披薩評分', max_digits=1, decimal_places=0, null=False,  
        validators=[MinValueValidator(1, '最低1分'), MaxValueValidator(5, '最多5分')])

    class Meta:
        unique_together=('member_id', 'pizza_no')

class CheckOrder(models.Model):
    order_no = models.OneToOneField(
        Order, verbose_name='訂單編號', on_delete=models.CASCADE, null=False)

    empolyee_id = models.ForeignKey(
        Employee, verbose_name='員工帳號', on_delete=models.CASCADE, null=False)

    profits = models.PositiveIntegerField(
        verbose_name='訂單利潤', null=False)

    class Meta:
        unique_together=('order_no', 'empolyee_id')