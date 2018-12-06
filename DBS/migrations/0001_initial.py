# Generated by Django 2.1.3 on 2018-12-05 09:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profits', models.PositiveIntegerField(verbose_name='訂單利潤')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='員工帳號')),
                ('title', models.CharField(max_length=8, verbose_name='員工職稱')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='會員帳號')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_no', models.AutoField(primary_key=True, serialize=False, verbose_name='訂單編號')),
                ('total_price', models.PositiveIntegerField(verbose_name='訂單總價')),
                ('ordered_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='訂單產生時間')),
                ('shipped_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='實際出貨時間')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=2, validators=[django.core.validators.MinValueValidator(0, '0<=使用者折扣<=1'), django.core.validators.MaxValueValidator(1, '0<=使用者折扣<=1')], verbose_name='使用者折扣')),
                ('details', models.TextField()),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DBS.Member', verbose_name='會員身分證號碼')),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('pizza_no', models.AutoField(primary_key=True, serialize=False, verbose_name='披薩編號')),
                ('name', models.CharField(max_length=20, verbose_name='披薩名稱')),
                ('description', models.TextField(verbose_name='披薩描述')),
                ('price', models.PositiveIntegerField(verbose_name='披薩價格')),
                ('size', models.CharField(max_length=2, verbose_name='披薩尺寸')),
                ('cost', models.PositiveIntegerField(verbose_name='披薩成本')),
                ('in_stock', models.PositiveIntegerField(verbose_name='披薩庫存量')),
                ('sales_volume', models.PositiveIntegerField(default=0, verbose_name='披薩銷售量')),
                ('click_count', models.PositiveIntegerField(default=0, verbose_name='披薩點擊量')),
                ('isVegetarian', models.BooleanField(verbose_name='是否為素食披薩')),
                ('stars', models.DecimalField(decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(1, '最低1分'), django.core.validators.MaxValueValidator(5, '最多5分')], verbose_name='披薩評分')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.DecimalField(decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(1, '最低1分'), django.core.validators.MaxValueValidator(5, '最多5分')], verbose_name='披薩評分')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DBS.Member', verbose_name='會員帳號')),
                ('pizza_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DBS.Pizza', verbose_name='披薩編號')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='使用者編號')),
                ('id_TW', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[A-Z]{1}[1-2]{1}[0-9]{8}$')], verbose_name='在台灣的身分證號碼')),
                ('password', models.CharField(max_length=25, verbose_name='使用者密碼')),
                ('name', models.CharField(max_length=20, verbose_name='使用者姓名')),
                ('phone_number', models.CharField(max_length=15, verbose_name='使用者電話號碼')),
                ('address', models.TextField(verbose_name='使用者住址')),
                ('age', models.PositiveIntegerField(verbose_name='使用者年齡')),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1, verbose_name='使用者性別')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=2, validators=[django.core.validators.MinValueValidator(0, '0<=使用者折扣<=1'), django.core.validators.MaxValueValidator(1, '0<=使用者折扣<=1')], verbose_name='使用者折扣')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DBS.User', verbose_name='會員的使用者編號'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DBS.User', verbose_name='員工的使用者編號'),
        ),
        migrations.AddField(
            model_name='checkorder',
            name='empolyee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DBS.Employee', verbose_name='員工帳號'),
        ),
        migrations.AddField(
            model_name='checkorder',
            name='order_no',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DBS.Order', verbose_name='訂單編號'),
        ),
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together={('member_id', 'pizza_no')},
        ),
        migrations.AlterUniqueTogether(
            name='checkorder',
            unique_together={('order_no', 'empolyee_id')},
        ),
    ]
