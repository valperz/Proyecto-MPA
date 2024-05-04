from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    """
    Formulario para facilitar la creación y edición de productos.
    """

    class Meta: 
        #Espeficiar a que modelo está asociado el formulario
        model = Producto

        fields = [
            'nombre',
            'cantidad',
            'presentacion',
            'fecha_creacion'
        ]

        labels = {
          
            'nombre':'Nombre',
            'cantidad':'Cantidad',
            'presentacion':'Presentacion',
            'fecha_creacion':'Fecha Creacion'
        }

        widgets = {
        
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'cantidad':forms.Textarea(attrs={'class':'form-control'}),
            'presentacion':forms.Textarea(attrs={'class':'form-control'}),
            'fecha_creacion':forms.NumberInput(attrs={'class':'form-control'}),

        }
    
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].error_messages = {'required': 'custom required message'}

        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'El campo {fieldname} es obligatorio'.format(
                fieldname=field.label)}