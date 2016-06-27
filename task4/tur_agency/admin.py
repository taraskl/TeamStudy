from django.contrib import admin

# Register your models here.
from .models import Country, City, Hotel, Tour, Client, Phone, Email, OrderStatus, Order

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Hotel)
admin.site.register(Tour)
admin.site.register(Client)
admin.site.register(Phone)
admin.site.register(Email)
admin.site.register(OrderStatus)
admin.site.register(Order)
