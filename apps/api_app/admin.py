from django.contrib import admin
from .models import CartItem, Species, Menu, Person

admin.site.register(Species)
admin.site.register(CartItem)
admin.site.register(Person)
admin.site.register(Menu)
#