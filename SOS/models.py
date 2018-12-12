from django.db import models
from MCS.models import Member
import django.utils.timezone as timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Order(models.Model):
    order_no = models.AutoField(
    	verbose_name='訂單編號', null=False, primary_key=True)

    # 哪一個 會員 產生的訂單
    member_id = models.ForeignKey(
        Member, verbose_name='會員編號', on_delete=models.CASCADE, null=False)
    total_price = models.PositiveIntegerField(
    	verbose_name='訂單總價', null=False)
    ordered_date = models.DateTimeField(
    	verbose_name='訂單產生時間', default=timezone.now, null=False)

    # 若為 null 代表 尚未出貨
    shipped_date = models.DateTimeField(
    	verbose_name='實際出貨時間', default=timezone.now)
    discount = models.DecimalField(
        verbose_name='訂單折扣', max_digits=2, decimal_places=2, null=False, 
        validators=[MinValueValidator(0, '0 <= 訂單折扣 <= 1'), MaxValueValidator(1, '0 <= 訂單折扣 <= 1')])    

    # 訂單內容: 裡面有從購物車送出的字串資訊
    details = models.TextField(null=False)

    # 訂單狀態
    def GetState():
    	if shipped_date!=null : return "已出貨"
    	return "訂單處理中"