# Generated by Django 2.1.3 on 2018-12-24 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MCS', '0003_auto_20181216_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Employee', to=settings.AUTH_USER_MODEL, verbose_name='員工的使用者編號'),
        ),
    ]
