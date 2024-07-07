from django.contrib import admin
from .models import Place_order

class Place_order_admin(admin.ModelAdmin):

    list_display =  ('user','customer','Product','qty', 'orderdate', 'Stats')

admin.site.register(Place_order,Place_order_admin )
