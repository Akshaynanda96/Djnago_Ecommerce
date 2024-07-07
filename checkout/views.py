from django.shortcuts import render
from accounts.models import *
from cart.models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def checkout(request):
    
    user = request.user
    if user :
        all_obj = profileDetails.objects.get(user = user)
        item_in_cart = Carts.objects.filter(user = user)
        cat_count = Carts.objects.filter(user = request.user).count()
        shipping_charges = 70
        Subtotal = 0
        finalAmount = 0
        cart_products = [ p for p in Carts.objects.all() if p.user == request.user ]
        if cart_products :
            for i in cart_products:
                totalAmt =  i.qty * i.product.product_price
                Subtotal += totalAmt
            
            finalAmount = Subtotal + shipping_charges
        
        context = {
            
            'finalAmount':finalAmount,
            'Subtotal':Subtotal,
            'shipping_charges':shipping_charges,
            'all_obj':all_obj,
            'item_in_cart':item_in_cart,
            'cat_count':cat_count
        }

        return render (request , 'checkout/checkout.html', context)
    
    else:
        return render (request , 'accounts/Profile.html')
