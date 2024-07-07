from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from cart.models import Carts
from accounts.models import profileDetails
from .models import Place_order ,  Product
from django.shortcuts import get_object_or_404


def payment_done(request):
    
    user = request.user
    cartid = request.GET.get('custid')
    customerdetails = profileDetails.objects.get(udid=cartid)
    cartdetails = Carts.objects.filter(user=user)

    
    
    for cart in cartdetails:
        product_instance = get_object_or_404(Product, udid=cart.product.udid)
        Place_order.objects.create(
            user=user,
            customer=customerdetails,
            Product=product_instance,
            qty=cart.qty
        ).save()
        cart.delete()
        
    return render(request, 'order/orders.html')


def order(request):
    cat_count = Carts.objects.filter(user = request.user).count()
    order_obj = Place_order.objects.filter(user = request.user)
    context = {
        'order_obj': order_obj,
        'cat_count':cat_count,
        
    }
    return render (request , 'order/orders.html', context)
    

