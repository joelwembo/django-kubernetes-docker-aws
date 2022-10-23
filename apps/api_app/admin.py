from django.contrib import admin
from .models import CartItem, Species, Person

admin.site.register(Species)
admin.site.register(CartItem)
admin.site.register(Person)

#