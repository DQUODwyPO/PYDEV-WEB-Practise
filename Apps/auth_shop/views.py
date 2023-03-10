from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User

from ..cart_shop.models import WishList



class Login(View):
   def get(self, request):
       return render(request, "auth_shop/index.html")

   def post(self, request):
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(username=username, password=password)
           if user is not None:
               login(request, user)
               print(user)
               return redirect('home:index')
       return redirect('auth_shop:login')


class new_user(View):
   def get(self, request):
       return render(request, "auth_shop/create_account.html")

   def post(self, request):
       form = CustomUserCreationForm(data=request.POST)
       print("OK")
       if form.is_valid():
           username = form.cleaned_data.get('username')
           email = form.cleaned_data.get('email')
           password = form.cleaned_data.get('password1')
           print("OK2")
           user = User.objects.create_user(username=username, email=email, password=password)
           wish = WishList()
           wish.user = user
           wish.save()
           user.save()
           return redirect('home:index')
       print(form.errors)
       return redirect('auth_shop:new_user')
