from django.contrib import admin

from django.contrib import admin
from .models import WishList, WishItem, Product

admin.site.register(WishList)
admin.site.register(WishItem)
admin.site.register(Product)