from django.contrib import admin
from accounts.models import Profile , profileDetails


class profile_details_Admin(admin.ModelAdmin):

    list_display = ('user', 'First_name', 'Last_name', 'sate_name', 'city_name', 'Addresses', 'pincode')
    search_fields = ('First_name', 'Last_name', 'sate_name','city_name' ,'user__username')
    list_filter = ('sate_name',)

admin.site.register( Profile)
admin.site.register(profileDetails,profile_details_Admin )
