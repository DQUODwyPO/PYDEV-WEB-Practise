from django.urls import path

from .views import checkoutShopView

app_name = 'checkout'

urlpatterns = [
   path('checkout', checkoutShopView.as_view(), name='checkout'),
]
