from django.urls import path

from .views import *

app_name = 'home'

urlpatterns = [
   path('', IndexShopView.as_view(), name='index'),
   ###path('shop/', shopShopView.as_view(), name='shop'),
   ###path('wishlist/', wishlistShopView.as_view(), name='wishlist'),
   ###path('product-single/', productShopView.as_view(), name='product-single'),
   ###path('cart/', cartShopView.as_view(), name='cart'),
   ###path('checkout/', checkoutShopView.as_view(), name='checkout'),
   path('about/', aboutShopView.as_view(), name='about'),
   ###path('blog/', blogShopView.as_view(), name='blog'),
   path('contact/', contactShopView.as_view(), name='contact'),
]
