from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (ListadoAutor,ActualizarAutor,EliminarAutor, 
ListadoLibros,ActualizarLibro,EliminarLibro,CrearLibro,listar_autor)#,CrearLibros,CrearAutor)

urlpatterns=[
   # path('',Home ,name='index'),
   # path('crear_autor/',crearAutor ,name='crear_autor'),
   # path('listar_autor/',listarAutores ,name='listar_autor'),
  #  path('editar_autor/<int:id>',editarAutor ,name='editar_autor'),
  #  path('eliminar_autor/<int:id>',eliminarAutor ,name='eliminar_autor'),

  #  path('crear_autor/<int:pk>',login_required(CrearAutor.as_view()) ,name='crear_autor'),
    path('listar_autor/',login_required(ListadoAutor.as_view()) ,name='listar_autor'),
    path('editar_autor/<int:pk>',login_required(ActualizarAutor.as_view()) ,name='editar_autor'),
    path('eliminar_autor/<int:pk>',login_required(EliminarAutor.as_view()) ,name='eliminar_autor'),

    path('listar_libros/',login_required(ListadoLibros.as_view()) ,name='listar_libros'),
    path('crear_libro/',CrearLibro.as_view(), name = 'crear_libro'),
  #  path('crear_libros/',CrearLibros.as_view() ,name='crear_libros'),
    path('editar_libro/<int:pk>',login_required(ActualizarLibro.as_view()) ,name='editar_libro'),
    path('eliminar_libro/<int:pk>',login_required(EliminarLibro.as_view()) ,name='eliminar_libro')


    

]