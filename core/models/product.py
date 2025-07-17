from django.db import models 
from libs.models import TimeInfo 
from .category import Category, Brand 
from tinymce.models import HTMLField 


class Product(TimeInfo):
    STOCK_STATUS = (
        (0, 'Out Of Stock'),
        (1, 'In Stock')
    )

    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    sku = models.CharField(max_length=255, null=True, blank=True)
    short_description = models.CharField(max_length=255)
    description = HTMLField(null=True, blank=True)
    price = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    sale_price = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    quantity = models.SmallIntegerField(default=0)
    stock_status = models.SmallIntegerField(default=1, choices=STOCK_STATUS)
    manage_stock = models.BooleanField(default=False)


    class Meta:
        db_table = 'products'
        verbose_name_plural = 'Product'


    def __str__(self):
        return f"{self.name} - {self.sku}"