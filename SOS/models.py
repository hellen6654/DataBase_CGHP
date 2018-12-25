from django.db import models
from MCS.models import Member
from PSMS.models import Pizza
import django.utils.timezone as timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Discount(models.Model):
    code = models.AutoField(
        verbose_name='折扣代碼', primary_key=True)

    name = models.CharField(
        verbose_name='折扣名稱', unique=True, max_length=20, null=False)

    description = models.TextField(
        verbose_name='折扣描述', default='')

    rate = models.DecimalField(
        max_digits=3, decimal_places=2, default=1, null=False, verbose_name='折扣率',
        validators=[MinValueValidator(0, '0<=折扣<=1'), MaxValueValidator(1, '0<=折扣<=1')])

    DISCOUNT_TYPE = (
        ('shipping', '運費'),
        ('seasoning', '季節性折扣'),
        ('special', '特殊折扣')
    )

    kind = models.CharField(
        verbose_name='種類', choices=DISCOUNT_TYPE, max_length=10, null=False, default='shipping')

    def __str__(self):
        return self.name

class DiscountFare(models.Model):
    discount_code = models.OneToOneField(
        Discount, verbose_name='折扣代碼', primary_key=True, on_delete=models.CASCADE)

    sill = models.PositiveIntegerField(
        verbose_name='目標金額', null=False)

class DiscountOrder(models.Model):
    discount_code = models.OneToOneField(
        Discount, verbose_name='折扣代碼', primary_key=True, on_delete=models.CASCADE)

    startDate = models.DateTimeField(
        verbose_name='優惠開始日期', null=False)

    endDate = models.DateTimeField(
        verbose_name='優惠截止日期', null=False)

    def getRate(self):
        return float(self.discount_code.rate)

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
        verbose_name='實際出貨時間', default=timezone.now)

    isFreeShipping = models.BooleanField(default=False)

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

    # 運費
    def getFare(self):
        BASIC_FARE = 60
        if isFreeShipping:
            return 0
        return BASIC_FARE

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

class DiscountItem(models.Model):
    order = models.ForeignKey(Order, related_name='theOrder', on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, related_name='theDiscount', on_delete=models.CASCADE)