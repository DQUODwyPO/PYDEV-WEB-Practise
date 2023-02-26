import django.contrib.auth.models
from django.shortcuts import render, redirect
from django.views import View
from ..cart_shop.models import Product, WishItem, WishList

class IndexShopView(View):

    def get(self, request):
        product_items = Product.objects.values()
        mas = []
        for prod in product_items:
            mas.append(prod)
        #print(product_items)
        context = dict()
        context['data'] = mas
        #context = {'data': [{'name': 'Bell Pepper',
        #                     'discount': 30,
        #                     'price_before': 120.00,
        #                     'price_after': 80.00,
        #                     'url': 'shop/images/product-1.jpg'},
        #                    {'name': 'Strawberry',
        #                     'discount': None,
        #                     'price_before': 120.00,
        #                     'url': 'shop/images/product-2.jpg'},
        #                    {'name': 'Green Beans',
        #                     'discount': None,
        #                     'price_before': 120.00,
        #                     'url': 'shop/images/product-3.jpg'},
        #                    {'name': 'Purple Cabbage',
        #                     'discount': None,
        #                     'price_before': 120.00,
        #                     'url': 'shop/images/product-4.jpg'},
        #                    {'name': 'Tomatoe',
        #                     'discount': 30,
        #                     'price_before': 120.00,
        #                     'price_after': 80.00,
        #                     'url': 'shop/images/product-5.jpg'},
        #                    {'name': 'Brocolli',
        #                     'discount': None,
        #                     'price_before': 120.00,
        #                     'url': 'shop/images/product-6.jpg'},
        #                    {'name': 'Carrots',
        #                     'discount': None,
        #                     'price_before': 120.00,
        #                     'url': 'shop/images/product-7.jpg'},
        #                    {'name': 'Fruit Juice',
        #                     'discount': None,
        #                     'price_before': 120.00,
        #                     'url': 'shop/images/product-8.jpg'},
        #                    ]
        #           }

        return render(request, 'home/index.html', context)


def add_wishitem(request, id):
    print(request.user)
    if str(request.user) is 'AnonymousUser':
        return redirect('auth_shop:login')
    prod = Product.objects.get(id=id)
    item = WishItem()
    item.product = prod
    item.WishList = WishList.objects.get(user=request.user)
    item.save()
    return redirect('home:index')

class aboutShopView(View):

    def get(self, request):
        return render(request, 'home/about.html')


class contactShopView(View):

    def get(self, request):
        return render(request, 'home/contact.html')
