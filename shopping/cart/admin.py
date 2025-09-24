from django.contrib import admin

# Register your models here.
from .models import CartModel
admin.site.register(CartModel)