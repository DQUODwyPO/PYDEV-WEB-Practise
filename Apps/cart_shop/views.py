from django.shortcuts import render, redirect
from django.views import View
from ..cart_shop.models import WishItem

class wishlistShopView(View):

    def get(self, request):
        if str(request.user) is 'AnonymousUser':
            return redirect('auth_shop:login')
        wishlish = WishItem.objects.filter(WishList__user=request.user)
        context = dict()
        mas = []
        for p in wishlish:
            a = dict()
            a['id'] = p.id
            a['url'] = p.product.url
            a['name'] = p.product.name
            if p.product.price_after is not None:
                a['price_before'] = p.product.price_after
            else:
                a['price_before'] = p.product.price_before
            mas.append(a)
        context['data'] = mas
        print(context)
        return render(request, 'cart_shop/wishlist.html', context)

def del_wish_item(request, id):
    WishItem.objects.filter(id=id).delete()
    return redirect('cart_shop:wishlist')


class cartShopView(View):

    def get(self, request):
        return render(request, 'cart_shop/cart.html')
