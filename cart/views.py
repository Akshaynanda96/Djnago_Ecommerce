from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from django.db.models import Q





def cart(request):

    user = request.user
    
    get_id = request.GET.get('cart_id')
    produc_name = Product.objects.get(udid = get_id)
    create_cart = Carts.objects.create(
        user = user,
        product =produc_name,
    )
    create_cart.save()
    return redirect( '/cart/' )


@login_required(login_url='accounts/login')
def cartdetails(request):

    user = request.user    
    addcat = Carts.objects.filter(user = user)

    totalAmt  = 0
    Subtotal = 0
    shipping_charges = 70
    finalAmount = 0

    cart_products = [ p for p in Carts.objects.all() if p.user == user ]

    if cart_products:
        for i in cart_products:
            totalAmt =  i.qty * i.product.product_price
            Subtotal += totalAmt
            finalAmount = Subtotal - shipping_charges

        context = {
            'addcat':addcat,
            'totalAmt':totalAmt,
            'Subtotal':Subtotal,
            'shipping_charges':shipping_charges,
            'finalAmount':finalAmount
        }
            
        return render(request , 'cart/cart.html', context)
    
    else:
        return render(request , 'cart/emptycart.html', context)



def qty_plus(request):
    if request.method == "GET":
        pro_id = request.GET.get('pro_id')
        
        # Fetch all cart items for the specific product and user
        cart_items = Carts.objects.filter(Q(product_id=pro_id) & Q(user=request.user))

        if cart_items.exists():
            # Loop through all cart items and update their quantity
            for cart_item in cart_items:
                cart_item.qty += 1
                cart_item.save()

            totalAmt = 0
            Subtotal = 0
            shipping_charges = 70

            cart_products = Carts.objects.filter(user=request.user)

            if cart_products.exists():
                for i in cart_products:
                    totalAmt = i.qty * i.product.product_price
                    Subtotal += totalAmt

                finalAmount = Subtotal + shipping_charges

                # Get the updated quantity from the first cart item
                updated_qty = cart_items.first().qty

                data = {
                    'qty': updated_qty,
                    'Subtotal': Subtotal,
                    'finalAmount': finalAmount,
                    'totalAmt':totalAmt
                }
                return JsonResponse(data)
        else:
            return JsonResponse({'error': 'No cart items found for this product'}, status=404)

    return JsonResponse({'error': 'Invalid request'}, status=400)


