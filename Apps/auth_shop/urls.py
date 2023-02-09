from django.urls import path
from .views import *

app_name = "auth_shop"

urlpatterns = [
  path('', Login.as_view(), name="login"),
  path('new_user', new_user.as_view(), name="new_user"),
]
