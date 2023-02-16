from django.shortcuts import render
from django.views import View


class wishlistShopView(View):

    def get(self, request):
        return render(request, 'cart_shop/wishlist.html')


class cartShopView(View):

    def get(self, request):
        return render(request, 'cart_shop/cart.html')
