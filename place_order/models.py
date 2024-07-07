from django.db import models
from django.contrib.auth.models import User
from accounts.models import profileDetails
from project.models import Product
from base.models import BaseModole

Status_Choices = (
    
    ('Delivered','Delivered'),
    ('Pending', 'Pending'),
    ('Cancel', 'Cancel'),
    ('Accepted ', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the Way' , 'On the Way')
    
)
class Place_order(BaseModole):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='Mainuser' , blank=True, null=True)
    customer = models.ForeignKey(profileDetails, on_delete=models.CASCADE , related_name='customerdetails',  blank=True, null=True)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE , blank=True , null=True , related_name= 'allcartproduct')
    qty = models.PositiveIntegerField(default=1)
    orderdate = models.DateField(auto_now_add=True)
    Stats = models.CharField(choices= Status_Choices, default='Pending' ,max_length=100)

    
    def __str__(self) -> str:
        return  self.Product.product_name 
  