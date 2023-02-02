from django.urls import path

from .views import IndexShopView

app_name = 'shop'

urlpatterns = [
   path('shop', IndexShopView.as_view(), name='shop'),
]
