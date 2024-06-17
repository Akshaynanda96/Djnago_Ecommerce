from django.db import models
from base.models import BaseModole
from project.models import Product
from django.contrib.auth.models import User



class Carts(BaseModole):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey( Product, to_field='udid', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)

    