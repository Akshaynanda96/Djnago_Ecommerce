
from django.urls import path
from . import views

urlpatterns = [
    path('products/<sulg>', views.productsdetails, name='products' ),
    path('shop/<sulg>', views.SubCategory_details, name='shop'),
    path('itemdetails/<sulg>', views.itemdetails, name= 'itemdetails')
]
