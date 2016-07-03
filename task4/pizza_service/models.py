from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256, blank=True)
    phone = models.CharField(max_length=256, blank=True)
    address = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Pizza(models.Model):
	name = models.CharField(max_length=256)
	prise = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return "%s, prise: %s" % (self.name, self.prise)

class PaymentStatus(models.Model):
    PAYMENT_STATUS = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('E', 'Erorr'),
    )
    name = models.CharField(max_length=60, blank=True, null=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS)

    def __str__(self):
        return "%s, prise: %s" % (self.name, self.prise)

class Order(models.Model):
    client = models.ForeignKey("Client")
    pizza = models.ForeignKey("Pizza", blank=True, null=True)
    add = models.DateTimeField()
    edit = models.DateTimeField()
    order_amount = models.IntegerField(blank=True, null=True)
    all_payments = models.IntegerField(blank=True, null=True)

    payment_status = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return "#%s, client: %s" % (self.id, self.client)

class ClientOrders(Order):
 

	def __str__(self):
		return "#%s, client: %s" % (self.umberOrder, self.client)


       