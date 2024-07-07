from django.urls import path
from . import views 
from cart.views import cart 

urlpatterns = [
    path('login/',views.login_page, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('Singup/', views.registration_page , name='Singup'),
    path('activate/<email_token>/', views.email_active , name='activate'),
    path('Profile/' , views.profile_D ,  name='profile'),
    path('contact/',views.contact, name='contact'),
  
    
]
