from django.contrib import admin

# Register your models here.
from .models import Client, Auto, Driver, Order

admin.site.register(Client)
admin.site.register(Auto)
admin.site.register(Driver)
admin.site.register(Order)
