
from django.urls import path

from .views import RandomValue

urlpatterns = [
   path('random_value/', RandomValue.as_view()),
]

