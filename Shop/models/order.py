from .product import Product
from .customer import Customer
from django.db import models
import datetime

from Shop.models import customer


class Order(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orser_customer')
    quantity= models.IntegerField(default=1)
    price= models.IntegerField()
    adresse= models.CharField(max_length=50, default=" ", blank=True)
    phone= models.CharField(max_length=50, default=" ", blank=True)
    date= models.DateField(default=datetime.datetime.today())
    status= models.BooleanField(default=False)

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer= customer_id).order_by('-date')