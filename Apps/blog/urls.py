from django.urls import path

from .views import blogShopView

app_name = 'blog'

urlpatterns = [
   path('blog', blogShopView.as_view(), name='blog'),
]
