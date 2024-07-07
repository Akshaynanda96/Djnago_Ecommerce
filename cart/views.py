from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from django.db.models import Q
from django.shortcuts import get_object_or_404




@login_required(login_url='login')
def cart(request):
    
    if request.method == 'GET' and 'cart_id' in request.GET :
        get_id = request.GET.get('cart_id')
        try:
            produc_name = Product.objects.get(udid = get_id)
            create_cart = Carts.objects.create(
                user = request.user,
                product =produc_name,
            )
            create_cart.save()
            return redirect( '/cart/' )
        except Product.DoesNotExist:
            pass
        
    return redirect('/')
    

@login_required(login_url='login')
def cartdetails(request):

    user = request.user    
    addcat = Carts.objects.filter(user = user)

    totalAmt  = 0
    Subtotal = 0
    shipping_charges = 70
    finalAmount = 0
    cat_count = Carts.objects.filter(user = request.user).count()
    cart_products = [ p for p in Carts.objects.all() if p.user == request.user ]

    if cart_products:
        for i in cart_products:
            totalAmt =  i.qty * i.product.product_price
            Subtotal += totalAmt
            finalAmount = Subtotal + shipping_charges

        context = {
            'addcat':addcat,
            'totalAmt':totalAmt,
            'Subtotal':Subtotal,
            'shipping_charges':shipping_charges,
            'finalAmount':finalAmount,
            'cat_count':cat_count,
        }
            
        return render(request , 'cart/cart.html', context)
    
    else:
        return render(request , 'cart/emptycart.html')



def increment_quantity(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        c = Carts.objects.get(Q(product=prod_id) & Q(user = request.user))
        c.qty += 1
        c.save()
        
        totalAmt  = 0
        Subtotal = 0
        shipping_charges = 70
        finalAmount = 0
        cart_products = [ p for p in Carts.objects.all() if p.user == request.user ]
        
        
        
        for i in cart_products:
            totalAmt =  i.qty * i.product.product_price
            Subtotal += totalAmt
            finalAmount = Subtotal + shipping_charges
            
        data = {
            'qty':i.qty,
            'totalAmt':totalAmt,
            'Subtotal':Subtotal,
            'shipping_charges':shipping_charges,
            'finalAmount':finalAmount
        }
        
        return JsonResponse(data)
    
    
def decrement_quantity(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        c = Carts.objects.get(Q(product=prod_id) & Q(user = request.user))
        c.qty -= 1
        c.save()
        
        totalAmt  = 0
        Subtotal = 0
        shipping_charges = 70
        finalAmount = 0
        cart_products = [ p for p in Carts.objects.all() if p.user == request.user ]
        
        
        
        for i in cart_products:
            totalAmt =  i.qty * i.product.product_price
            Subtotal += totalAmt
            finalAmount = Subtotal + shipping_charges
            
        data = {
            'qty':i.qty,
            'totalAmt':totalAmt,
            'Subtotal':Subtotal,
            'shipping_charges':shipping_charges,
            'finalAmount':finalAmount
        }
        
        return JsonResponse(data)
    


def remove_to_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        print(prod_id)
        c = Carts.objects.get(Q(product=prod_id) & Q(user = request.user))    
        c.delete()
        
        totalAmt  = 0
        Subtotal = 0
        shipping_charges = 70
        finalAmount = 0
        cart_products = [ p for p in Carts.objects.all() if p.user == request.user ]
        
        
        
        for i in cart_products:
            totalAmt =  i.qty * i.product.product_price
            Subtotal += totalAmt
            finalAmount = Subtotal + shipping_charges
            
        data = {
            'totalAmt':totalAmt,
            'Subtotal':Subtotal,
            'shipping_charges':shipping_charges,
            'finalAmount':finalAmount
        }
        
        return JsonResponse(data)
    
    
