from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('search_box/',views.search_box, name='search_box'),
    path('offers/<slug>' , views.Discount , name='offers')
    
]
