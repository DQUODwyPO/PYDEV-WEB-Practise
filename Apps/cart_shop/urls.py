from django.urls import path

from Apps.home.views import *


urlpatterns = [
   path('cart', cartShopView.as_view(), name='cart'),
]
