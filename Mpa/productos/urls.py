from django.urls import path

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.productosIndex, name='productosIndex'),
    path('gestion/',views.gestionProductos, name='gestionProductos'),
]