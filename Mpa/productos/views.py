from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from datetime import datetime

from .forms import ProductoForm
from .models import Producto


# Create your views here.
def listar(request):
     #Consultar productos
    productos_list = Producto.objects.all()
    #Configurar paginación cada 10 productos
    paginator = Paginator(productos_list, 10)

    #Obtener página
    page_number = request.GET.get('page',0)
    page_obj = paginator.get_page(page_number)

    #Obtener el template
    template = loader.get_template("listar.html")
    #Agregar el contexto
    context = {"page_obj": page_obj}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

def agregarStock(request):
    #Obtener el template
    template = loader.get_template("agregarStock.html")
    #Generar Formulario
    if request.method == "POST":
        form = ProductoForm(request.POST or None, request.FILES)
        if form.is_valid():
            #obtener datos del formulario
            producto_nuevo = form.save(commit=False)
            #Asignar fecha de creación
            producto_nuevo.fecha_creacion = datetime.now()
            #Guardar Producto
            producto_nuevo.save()
            return redirect('listar')
    else:
        form = ProductoForm()
    #Crear contexto
    context = {}
    context['form'] = form
    
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))



def quitarStock(request):
    #Obtener el template
    template = loader.get_template("quitarStock.html")
    #Generar Formulario
    if request.method == "POST":
        form = ProductoForm(request.POST or None, request.FILES)
        if form.is_valid():
            #obtener datos del formulario
            producto_nuevo = form.save(commit=False)
            #Asignar fecha de creación
            producto_nuevo.fecha_creacion = datetime.now()
            #Guardar Producto
            producto_nuevo.save()
            return redirect('listar')
    else:
        form = ProductoForm()
    #Crear contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))