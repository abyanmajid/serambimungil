from django.contrib import admin
from .models import Product, Home, About

class Display_ID(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Product, Display_ID)
admin.site.register(Home, Display_ID)
admin.site.register(About, Display_ID)