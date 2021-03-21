from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import Inicio, Login,LogoutUsuario,RegistrarUsuario,ListadoUsuario,InicioListadoUsuario,EliminarUsuario,EditarUsuario

urlpatterns=[
    path('inicio_usuarios/',InicioListadoUsuario.as_view() ,name='inicio_usuarios'),
    path('login/',Login.as_view() ,name='login'),
  #  path('logout/',login_required(logoutUser) ,name='logout'),
    path('logout/',LogoutUsuario.as_view(next_page='accounts:login'),name='logout'),
    path('listado_usuarios/',ListadoUsuario.as_view(),name='listado_usuarios'),
    path('registrar_usuario/',RegistrarUsuario.as_view() ,name='registrar_usuario'),
    path('actualizar_usuario/<int:pk>/',EditarUsuario.as_view(), name = 'actualizar_usuario'),
    path('eliminar_usuario/<int:pk>/',EliminarUsuario.as_view(), name='eliminar_usuario'),

    
#BORRADO LOGIN_REQUIRED X LOGINREQUIREDMIXIN
]
