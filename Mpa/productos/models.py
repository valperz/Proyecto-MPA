from django.db import models

# Create your models here.
class Producto(models.Model):
    """
    Modelo que representa los productos que son vendidos en la tienda, 
    tiene asociada una categoria (que tambien esta asociada a un animal)
    y un estado
    """
    nombre = models.CharField(max_length=100)
    presentacion = models.CharField(max_length=30)
    cantidad= models.IntegerField()
    fecha_creacion = models.DateTimeField()

    def __str__(self):
        return self.nombre
    
class cambio_stock(models.Model):
    ref_producto= models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    tipo_cambio= models.CharField(max_length=20)
    comentario=models.CharField(max_length=100)
    fecha=models.DateTimeField()
