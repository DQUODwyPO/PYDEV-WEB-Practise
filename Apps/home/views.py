from django.shortcuts import render
from django.views import View


class IndexShopView(View):

    def get(self, request):
        return render(request, 'home/index.html')


class shopShopView(View):

    def get(self, request):
        return render(request, 'shop/shop.html')


class wishlistShopView(View):

    def get(self, request):
        return render(request, 'cart_shop/wishlist.html')


class productShopView(View):

    def get(self, request):
        return render(request, 'shop/product-single.html')


class cartShopView(View):

    def get(self, request):
        return render(request, 'cart_shop/cart.html')


class checkoutShopView(View):

    def get(self, request):
        return render(request, 'checkout/checkout.html')


class aboutShopView(View):

    def get(self, request):
        return render(request, 'home/about.html')


class blogShopView(View):

    def get(self, request):
        return render(request, 'blog/blog.html')


class contactShopView(View):

    def get(self, request):
        return render(request, 'home/contact.html')
