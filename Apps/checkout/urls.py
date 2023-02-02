from django.urls import path

from .views import IndexShopView

app_name = 'checkout'

urlpatterns = [
   path('checkout', IndexShopView.as_view(), name='checkout'),
]
