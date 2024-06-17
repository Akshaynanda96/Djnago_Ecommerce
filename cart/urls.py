from django.urls import path

from . import views

urlpatterns = [
    path('cart/', views.cartdetails, name='my_cart' ),
    path('addtocart/' ,views.cart , name= 'addcart'),
    path('pluscart/', views.qty_plus)
]
