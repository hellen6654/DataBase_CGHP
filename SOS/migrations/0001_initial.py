# Generated by Django 2.1.3 on 2018-12-10 05:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MCS', '0002_auto_20181210_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_no', models.AutoField(primary_key=True, serialize=False, verbose_name='訂單編號')),
                ('total_price', models.PositiveIntegerField(verbose_name='訂單總價')),
                ('ordered_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='訂單產生時間')),
                ('shipped_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='實際出貨時間')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=2, validators=[django.core.validators.MinValueValidator(0, '0 <= 訂單折扣 <= 1'), django.core.validators.MaxValueValidator(1, '0 <= 訂單折扣 <= 1')], verbose_name='訂單折扣')),
                ('details', models.TextField()),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MCS.Member', verbose_name='會員身分證號碼')),
            ],
        ),
    ]