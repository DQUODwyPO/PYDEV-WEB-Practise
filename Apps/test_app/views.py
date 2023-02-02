from random import randint

from django.views import View
from django.http import HttpResponse


class RandomValue(View):
   def get(self, request):
       html = f"{randint(0, 2**64)}"
       return HttpResponse(html)
