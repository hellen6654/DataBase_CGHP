# Generated by Django 2.1.3 on 2018-12-16 07:25

import MCS.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MCS', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='member',
            managers=[
                ('objects', MCS.models.CustomUserManager()),
            ],
        ),
    ]