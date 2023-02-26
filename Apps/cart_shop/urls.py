from django.urls import path

from .views import *

app_name = 'cart_shop'

urlpatterns = [
   path('cart', cartShopView.as_view(), name='cart'),
   path('wishlist', wishlistShopView.as_view(), name='wishlist'),
   path('remove_item/<int:id>/', del_wish_item, name='remove_item'),
]
