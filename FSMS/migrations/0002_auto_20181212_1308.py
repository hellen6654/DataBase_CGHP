# Generated by Django 2.1.3 on 2018-12-12 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FSMS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkorder',
            name='empolyee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MCS.Employee', verbose_name='員工編號'),
        ),
    ]
