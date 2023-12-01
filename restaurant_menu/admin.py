from django.contrib import admin
from .models import Item


# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("meal", "status")
    list_filter = ("status", "price")
    search_fields = ("meal", "description")


admin.site.register(Item, RestaurantAdmin)
