from django.contrib import admin
from cart.models import Carts



class CartAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'get_product_uuid', 'qty')

    def get_product_uuid(self, obj):
        return obj.product.udid
    get_product_uuid.short_description = 'Product UUID'

admin.site.register(Carts, CartAdmin)