# -*- coding: UTF-8 -*-
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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