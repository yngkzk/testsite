from django.contrib import admin
from .models import IceCream, IceCreamKiosk


class IceCreamAdmin(admin.ModelAdmin):
    list_display = ('flavor', 'price', 'portion_size', 'ingredients', 'calories')
    list_display_links = ('flavor',)
    search_fields = ('flavor', 'ingredients')


class IceCreamKioskAdmin(admin.ModelAdmin):
    list_display = ('location', 'available_flavors', 'prices', 'working_hours', 'staff_info', 'special_offers')
    list_display_links = ('location',)
    search_fields = ('location', 'available_flavors')


admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(IceCreamKiosk, IceCreamKiosk)
