from django.contrib import admin

# Register your models here.
from .models import Contact, RoiInvestment

admin.site.register(Contact)
admin.site.register(RoiInvestment)
