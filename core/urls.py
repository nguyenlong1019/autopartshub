from django.urls import path, re_path 
from core.views.index import *


urlpatterns = [
    path('', index_view, name='index_view'),
    path('gioi-thieu', about_view, name='about_view'),
    path('lien-he', contact_view, name='contact_view'),
    path('<category_slug>', product_by_category_view, name='product_by_category_view'),
    path('<category_slug>/<product_slug>', product_detail_view, name='product_detail_view'),
    re_path(r'^(?P<slug>.+)/$', static_page_view, name='static_page_view')
]
