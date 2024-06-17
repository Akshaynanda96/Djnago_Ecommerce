from django.shortcuts import render
import random
from datetime import timedelta
from django.utils import timezone
from project.models import *
from cart.models import Carts




def home(request):
    try :

        all_products = list(Product.objects.all())
        if len(all_products) > 8:
            products = random.sample(all_products, 8)
        else:
            products = all_products
# ---------------------------------------------------------------------

        thirty_days_ago = timezone.now() - timedelta(days=30)
        recent_products = Product.objects.filter(create_at__gte=thirty_days_ago)
        recent_products = list(recent_products)
        
        if len(recent_products) > 8:
            newproducts = random.sample(recent_products, 8)
        else:
            newproducts = recent_products
     
        category = Category.objects.all()

        
      
        context = {
            "data":products,
            'category':category,
            'newproduct':newproducts,
            
   
        }        
        return render(request , 'home/index.html', context)
    except Exception:
        return render(request , 'base/404.html')


