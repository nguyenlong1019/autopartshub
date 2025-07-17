from django.db import models 
from libs.models import TimeInfo 


class Category(TimeInfo):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=300, null=True, blank=True)


    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'Category'


    def __str__(self):
        return self.name 
    

class Brand(TimeInfo):
    name = models.CharField(max_length=255, unique=True)


    class Meta:
        db_table = 'brands'
        verbose_name_plural = 'Brand'

    
    def __str__(self):
        return self.name 
    