from django.urls import path

from . import views

urlpatterns = [
    path('cart/', views.cartdetails, name='my_cart' ),
    path('addtocart/' ,views.cart , name= 'addcart'),
    path('increment_quantity/', views.increment_quantity, name='increment_quantity'),
    path('decrement_quantity/', views.decrement_quantity, name='decrement_quantity'),
    path('remove_to_cart/', views.remove_to_cart, name='remove_to_cart'),
]
