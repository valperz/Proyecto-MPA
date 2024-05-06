from django.urls import path

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.listar, name='listar'),
    path('añadir/',views.agregarStock, name='agregarStock'),
    path('quitar/',views.quitarStock, name='quitarStock'),
    
]