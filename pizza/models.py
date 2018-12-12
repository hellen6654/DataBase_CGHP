from django.db import models
import django.utils.timezone as timezone
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Pizza(models.Model):
    pizza_no = models.PositiveIntegerField(
        verbose_name='披薩編號', primary_key=True, null=False) #pk
    name = models.CharField(
        verbose_name='披薩名字', max_length=8, null=False) #名字字數最長8個字
    description = models.TextField(
        verbose_name='內容簡介')
    price = models.DecimalField(
        verbose_name='披薩價格', max_digits=4, decimal_places=0, null=False,
        validators=[MinValueValidator(0, '最低0元'), MaxValueValidator(1000, '最貴1000元')]) #價錢0～1000 無小數 
    size = models.CharField(
        verbose_name='披薩尺寸', max_length=2, null=False) #大小6～20 
    cost = models.DecimalField(
        verbose_name='披薩成本', max_digits=4, decimal_places=0, null=False, 
        validators=[MinValueValidator(0, '最低0元'), MaxValueValidator(500, '最貴500元')]) #成本0～500 
    in_stock = models.DecimalField(
        verbose_name='披薩庫存', max_digits=2, decimal_places=0, null=False,  
        validators=[MinValueValidator(0, '最少0個'), MaxValueValidator(99, '最多99個')]) 
    sales_volume = models.DecimalField(
        verbose_name='披薩銷售量', max_digits=4, decimal_places=0, null=False, 
        validators=[MinValueValidator(0, '最少0個'), MaxValueValidator(500, '最好是賣這麼多')]) 
    click_count = models.DecimalField(
        verbose_name='披薩點擊量', max_digits=5, decimal_places=0, null=False, 
        validators=[MinValueValidator(0, '最少0次')]) #點擊數量 無上限
    isVegetarian = models.BooleanField(
        verbose_name='素食', null=False) #是否為素食
    stars = models.DecimalField(
        verbose_name='披薩評分', max_digits=1, decimal_places=0, null=False,  
        validators=[MinValueValidator(0, '最低0分'), MaxValueValidator(5, '最多5分')]) #小數
    def __str__(self):
        return self.name

class User(models.Model):
    FEMALE = 'F'
    MALE = 'M'
    user_id = models.CharField(
        verbose_name='身分證號碼', max_length=10, primary_key=True, null=False,
        validators=[RegexValidator(r'^[A-Z]{1}[1-2]{1}[0-9]{8}$')])
    password = models.CharField(
        verbose_name='使用者密碼', max_length=20, null=False)
    name = models.CharField(
        verbose_name='使用者姓名', max_length=20, null=False)
    phone_number = models.CharField(
        verbose_name='使用者電話號碼', max_length=15, null=False)
    address = models.CharField(
        verbose_name='使用者住址', max_length=64, null=False)
    age = models.DecimalField(
        verbose_name='使用者年齡', max_digits=3, decimal_places=0,
        validators=[MinValueValidator(0, '最低0歲')])

    GENDER_IN_USER_CHOICES = ((FEMALE, 'Female'), (MALE, 'Male'),)

    gender = models.CharField(
        verbose_name='使用者性別', max_length=1, choices=GENDER_IN_USER_CHOICES, null=False)
    discount = models.DecimalField(
        verbose_name='使用者折扣', max_digits=2, decimal_places=2, null=False, 
        validators=[MinValueValidator(0, '0<=使用者折扣<=1'), MaxValueValidator(1, '0<=使用者折扣<=1')])
    def __str__(self):
        return self.name

class Member(models.Model):
    user_id = models.ForeignKey(
        User, verbose_name='會員身分證號碼', on_delete=models.CASCADE, null=False)
    member_id = models.CharField(
        verbose_name='會員編號', max_length=32, null=False)


class Employee(models.Model):
    user_id = models.ForeignKey(
        User, verbose_name='員工身分證號碼', on_delete=models.CASCADE, null=False)
    employee_id = models.CharField(
        verbose_name='員工編號', max_length=32, null=False, primary_key=True)
    title = models.TextField(
        verbose_name='員工職稱', max_length=32, null=False)

class Rate(models.Model):
    member_id = models.ForeignKey(
        Member, verbose_name='會員身分證號碼', on_delete=models.CASCADE, null=False)
    pizza_no = models.OneToOneField(
        Pizza, verbose_name='披薩編號', on_delete=models.CASCADE, null=False)
    stars = models.DecimalField(
        verbose_name='披薩評分', max_digits=1, decimal_places=0, null=False,  
        validators=[MinValueValidator(0, '最低0分'), MaxValueValidator(5, '最多5分')]) #小數
    class meta:
        unique_together=('member_id', 'pizza_no')

class Order(models.Model):
    order_no = models.PositiveIntegerField(verbose_name='訂單編號', null=False, primary_key=True) #pk
    member_id = models.ForeignKey(
        Member, verbose_name='會員身分證號碼', on_delete=models.CASCADE, null=False)
    total_price = models.DecimalField(verbose_name='訂單總價', max_digits=10, decimal_places=0, null=False)
    ordered_date = models.DateTimeField(verbose_name='訂單產生時間', default=timezone.now, null=False)
    shipped_date = models.DateTimeField(verbose_name='實際出貨時間', default=timezone.now, null=False)
    discount = models.DecimalField(
        verbose_name='使用者折扣', max_digits=2, decimal_places=2, null=False, 
        validators=[MinValueValidator(0, '0<=使用者折扣<=1'), MaxValueValidator(1, '0<=使用者折扣<=1')])
    details = models.ManyToManyField(Pizza)


class CheckOrder(models.Model):
    order_no = models.OneToOneField(
        Order, verbose_name='訂單編號', on_delete=models.CASCADE, null=False)
    empolyee_id = models.ForeignKey(
        Employee, verbose_name='員工編號', on_delete=models.CASCADE, null=False)
    profits = models.DecimalField(
        verbose_name='訂單利潤', max_digits=4, decimal_places=0, null=False,
        validators=[MinValueValidator(0, '最少0元')])
    class meta:
        unique_together=('order_no', 'empolyee_id')