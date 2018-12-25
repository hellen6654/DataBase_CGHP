from django.db import models
from MCS.models import Member
from PSMS.models import Pizza
import django.utils.timezone as timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Order(models.Model):
    order_no = models.AutoField(
        verbose_name='訂單編號', null=False, primary_key=True)

    member_id = models.ForeignKey(
        Member, verbose_name='會員編號', on_delete=models.CASCADE, null=False) # 哪一個 會員 產生的訂單

    ordered_date = models.DateTimeField(
        verbose_name='訂單產生時間', auto_now_add=True, null=False)

    updated = models.DateTimeField(auto_now=True)

    paid = models.BooleanField(verbose_name='是否付款',default=False) # 若為 true 代表 出貨

    shipped_date = models.DateTimeField(
        verbose_name='實際出貨時間', blank=True, null=True)
        
    class Meta:
        ordering = ['-ordered_date',]

    def __str__(self):
        return 'Order {}'.format(self.order_no)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    # 訂單狀態
    def GetState(self):
    	if self.paid : 
            return "已出貨"
    	return "訂單處理中"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

