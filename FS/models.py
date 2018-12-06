# -*- coding: UTF-8 -*-
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from MCS.models import Member
from PSMS.models import Pizza

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