# Generated by Django 2.1.3 on 2018-12-24 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FSMS', '0002_auto_20181216_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkorder',
            name='sold_date',
            field=models.DateTimeField(auto_now=True, verbose_name='出貨時間'),
        ),
    ]
