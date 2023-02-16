from django.urls import path

from .views import *

app_name = 'shop'

urlpatterns = [
   path('shop/', shopShopView.as_view(), name='shop'),
   path('product-single/', productShopView.as_view(), name='product-single')
]
