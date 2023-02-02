"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
   path('admin/', admin.site.urls),
   path('other/', include('Apps.login.urls')),
   path('other/', include('Apps.test_app.urls')),
   path('other/', include('Apps.common.urls')),
   #path('other/cart/', include('Apps.cart.urls')),
   path('', include('Apps.home.urls')),
   #path('', include('Apps.shop.urls')),
   #path('', include('Apps.blog.urls')),
   #path('', include('Apps.cart_shop.urls')),
   #path('', include('Apps.checkout.urls')),
]