from PIL import Image
from django.db import models


from django.contrib.auth.models import User


class WishList(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return f"{self.user}"

#import sqlite3
#sqlite3.connect('')

class Product(models.Model):
   id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
   name = models.CharField(max_length=255)
   price_before = models.DecimalField(max_digits=10, decimal_places=2)
   price_after = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
   discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
   url = models.ImageField(upload_to='static/shop/images/', null=True, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def save(self, *args, **kwargs):
      super().save(*args, **kwargs)
      img = Image.open(self.url.path)
      #img = img.resize((400, 400), Image.ANTIALIAS)
      img.save(self.url.path)

   def __str__(self):
       return self.name


class WishItem(models.Model):
   id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
   WishList = models.ForeignKey(WishList, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return f"{self.WishList}_{self.product}"
   class Meta:
      unique_together = ["WishList", "product"]


   # Create your models here.
