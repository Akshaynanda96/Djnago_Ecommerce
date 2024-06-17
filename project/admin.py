from django.contrib import admin
from .models import *


class sub_categoryAdmin(admin.ModelAdmin):
    list_display = ['subcategory_name']

class CatergoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']

class Product_ImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_category','product_subcategory',
                    'product_name','product_price','product_decribstion',
                    'product_Brand','product_artical',
                   ]

    search_fields = ['product_category','product_subcategory',
                    'product_name','product_price',
                    'product_Brand','product_artical',
                     ]

    inlines = [Product_ImageAdmin]

admin.site.register(Size_variations)
admin.site.register(color_variations)
admin.site.register(Category ,CatergoryAdmin )
admin.site.register(Product , ProductAdmin)
admin.site.register(SubCategory , sub_categoryAdmin)
