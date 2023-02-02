from django.urls import path

from .views import IndexShopView

app_name = 'blog'

urlpatterns = [
   path('blog', IndexShopView.as_view(), name='blog'),
]
