from django.urls import path
from . import views

urlpatterns = [
    path('payment_done/', views.payment_done, name='payment_done' ),
    path('order/', views.order, name='order' ),
]
