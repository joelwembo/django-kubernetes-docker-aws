from itertools import product
from django.contrib import admin

# Register your models here.
from .models import Price, Product

admin.site.register(Product)
admin.site.register(Price)
