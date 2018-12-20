# -*- coding: UTF-8 -*-
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
class Pizza(models.Model):
    pizza_no = models.AutoField(
        verbose_name='披薩編號', primary_key=True, null=False)
    slug = models.SlugField(max_length=128,default='0')
    name = models.CharField(
        verbose_name='披薩名稱', max_length=20, null=False)
    element = models.TextField(
        verbose_name='披薩餡料', null=True)
    description = models.TextField(
        verbose_name='披薩描述', max_length=50)
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
    kind_chose = (
        ('Beef', '牛肉'),
        ('Chicken', '雞肉'),
        ('Mix', '混合'),
        ('Pork', '豬肉'),
        ('Seafood', '海鮮'),
        ('Vegetable', '蔬菜') 
    )
    kind = models.CharField(
        verbose_name='種類', choices=kind_chose, max_length=10, null=True)
    stars = models.DecimalField(
        verbose_name='披薩評分', max_digits=1, decimal_places=0, null=False,   
        validators=[MinValueValidator(1, '最低1分'), MaxValueValidator(5, '最多5分')])
    pic = models.ImageField(upload_to='pizza-imgae/', null=True)
    available = models.BooleanField(verbose_name='上架',default=False)
    def starsCounter(self):
        return range(int(self.stars))
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs=[self.id])