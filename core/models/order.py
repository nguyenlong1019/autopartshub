from django.db import models 
from libs.models import TimeInfo 
from .user import User 
from .product import Product 



class Order(TimeInfo):
    ORDER_STATUS = (
        (0, 'Draft'),
        (1, 'Pending'),
        (2, 'Approved'),
        (3, 'Ready to Ship'),
        (4, 'Shipping'),
        (5, 'Completed'),
        (6, 'Cancelled'),
        (7, 'Refunded'),
        (8, 'Partially Refunded'),
        (9, 'Rejected')
    )

    FULFILLMENT_STATUS = (
        (0, 'Unfulfilled'),
        (1, 'Fulfilled')
    )

    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='customer')
    fullname = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    shipping_address = models.TextField(null=True, blank=True)
    order_status = models.SmallIntegerField(default=1, choices=ORDER_STATUS)
    fulfillment_status = models.SmallIntegerField(default=0, choices=FULFILLMENT_STATUS)
    total = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True, help_text='Tổng số tiền hàng')
    shipping_fee = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True, help_text='Phí vận chuyển')
    tax_fee = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True, help_text='Thuế')
    sub_total = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True, verbose_name='Tổng chi phí đơn hàng (Tổng tiền hàng hóa + phí ship + thuế)')
    staff_process = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='employee')


    class Meta:
        db_table = 'orders'
        verbose_name_plural = 'Order'


class OrderItem(TimeInfo):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.SmallIntegerField(default=1)
    total = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True)


    class Meta:
        db_table = 'order_items'
        verbose_name_plural = 'Order Item'
