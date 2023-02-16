from django.shortcuts import render
from django.views import View


class productShopView(View):

    def get(self, request):
        return render(request, 'shop/product-single.html')

class shopShopView(View):

    def get(self, request):
        return render(request, 'shop/shop.html')

