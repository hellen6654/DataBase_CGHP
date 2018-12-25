from django.db import models
from MCS.models import Employee
from SOS.models import Order

# Create your models here.
class CheckOrder(models.Model):
    order_no = models.OneToOneField(
        Order, verbose_name='訂單編號', on_delete=models.CASCADE, null=False)

    employee_id = models.ForeignKey(
        Employee, verbose_name='員工編號', on_delete=models.CASCADE, null=False)

    profits = models.PositiveIntegerField(
        verbose_name='訂單利潤', null=False)

    class Meta:
        unique_together=('order_no', 'employee_id')