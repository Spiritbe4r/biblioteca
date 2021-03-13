from django import forms
from django.forms import widgets
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model=Autor
        fields=['nombre','apellidos','nacionalidad','descripcion']
        labels={
            'nombre':'Nombre del autor',
            'apellidos':'Apellidos del autor',
            'nacionalidad':'Nacionalidad del autor',
            'descripcion':'Pequeña descripcion'
        }
        widgets={
            'nombre':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del Autor',
                    'id':'nombre'
                }
            ),

            'apellidos':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese los Apellidos del Autor',
                    'id':'apellidos'
                }
            ),
            'nacionalidad':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese la Nacionalidad del Autor',
                    'id':'nacionalidad'
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese una descripción del Autor',
                    'id':'descripcion'
                }
            )
        }
'''
class ReservaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['libro'].queryset = Libro.objects.filter(estado = True,cantidad__gte = 1)

    class Meta:
        model = Reserva
        fields = '__all__'
    
    def clean_libro(self):
        libro = self.cleaned_data['libro']
        if libro.cantidad < 1:
            raise ValidationError('No se puede reservar este libro, deben existir unidades disponibles.')

        return libro'''

class LibroForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['autor_id'].queryset = Autor.objects.filter(estado = True)
    

    class Meta:
        model = Libro
        fields = ('titulo','autor_id','fecha_publicacion','descripcion')#,'imagen','cantidad')
        label = {
            'titulo':'Título del libro',
            'autor_id': 'Autor(es) del Libro',
            'fecha_publicacion': 'Fecha de Publciación del Libro'
        }
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese título de libro'
                }
            ),
            'autor_id': forms.SelectMultiple(
                attrs = {
                    'class':'form-control'
                }
            ),
            'fecha_publicacion': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control'
                }
            )
        }

