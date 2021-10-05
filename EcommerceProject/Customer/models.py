
from django.db import models
from Accounts.models import Customer,CustomUser
from Seller.models import Laptop,Grocery,Mobile

class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    laptop=models.ForeignKey(Laptop,on_delete=models.CASCADE,null=True)
    mobile=models.ForeignKey(Mobile,on_delete=models.CASCADE,null=True)
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE, null=True)
    price=models.IntegerField()
    quantity=models.IntegerField()

    # def __str__(self):
    #     return f'{self.customer.name}'