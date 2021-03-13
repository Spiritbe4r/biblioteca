from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import Login,LogoutUsuario,RegistrarUsuario,ListadoUsuario

urlpatterns=[
  
    path('login/',Login.as_view() ,name='login'),
  #  path('logout/',login_required(logoutUser) ,name='logout'),
    path('logout/',login_required(LogoutUsuario.as_view(next_page='accounts:login')) ,name='logout'),
    path('list_users/',login_required(ListadoUsuario.as_view()) ,name='list_users'),
    path('register/',login_required(RegistrarUsuario.as_view()) ,name='register_users'),

    

]
