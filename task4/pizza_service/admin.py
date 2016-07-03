from django.contrib import admin

# Register your models here.
from .models import Client, Pizza, Order, PaymentStatus

admin.site.register(Client)
admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(PaymentStatus)
