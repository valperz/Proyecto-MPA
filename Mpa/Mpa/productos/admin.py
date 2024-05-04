from django.contrib import admin
from .models import Producto,cambio_stock
# Register your models here.

admin.site.register(Producto)
admin.site.register(cambio_stock)