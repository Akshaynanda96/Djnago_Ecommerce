from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse

from project.models import *
from cart.models import *

def productsdetails(request, sulg):
 
    try:
        category = get_object_or_404(Category, slugField=sulg)
        products = Product.objects.filter(product_category=category)
        subcategories = SubCategory.objects.filter(products__in=products).distinct()
        
        context = {
        'subcat':subcategories,
        "products":products,
        "category":category
        }

        return render(request, 'productdetails/subcat.html', context)

    except Product.DoesNotExist:
        return render(request, 'base/404.html')



def SubCategory_details(request,sulg):

    subcategory = get_object_or_404(SubCategory, slugField=sulg)
    products = Product.objects.filter(product_subcategory=subcategory)
    context = {
        'products': products,
    }

    return render(request, 'productdetails/subwiseproduct.html', context)



def itemdetails(request , sulg):

    data = get_object_or_404(Product, slugField=sulg)

    context = {
        'data':data,
    }
    
    return render(request, 'productdetails/detail.html', context)

    

