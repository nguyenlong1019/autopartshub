from django.db import models 
from libs.models import TimeInfo
from .product import Product


class ProductImage(TimeInfo):
    IMAGE_TYPE = (
        (0, 'Main Image'),
        (1, 'Detail Image'),
        (2, 'Thumb Image')
    )
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    type = models.SmallIntegerField(default=1, choices=IMAGE_TYPE)
    is_default = models.BooleanField(default=False)


    class Meta:
        db_table = 'product_images'
        verbose_name_plural = 'Product Image'


    
