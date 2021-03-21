from .mixins import LoginYSuperStaffMixin
from django.views.generic import TemplateView
from .models import Usuario
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic import ListView
from django.contrib.auth import login,logout
from django.contrib.auth.views import LogoutView
from .forms import FormularioLogin, FormularioUsuario, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class Inicio(LoginYSuperStaffMixin,TemplateView):
    template_name='sb_admin2/body.html'  

# Create your views here.
class Login(FormView):
    template_name = 'users/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)
'''
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('accounts:login')'''


class LogoutUsuario(LoginRequiredMixin,LogoutView):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)

class InicioListadoUsuario(LoginRequiredMixin,TemplateView):
    template_name = "users/listar_usuario.html"
   


class ListadoUsuario(LoginRequiredMixin,ListView):
    model = Usuario
    

    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            data=serialize('json',self.get_queryset())
            return HttpResponse(data,'application/json')
        else:
            return redirect('accounts:inicio_usuarios')
    '''
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            lista_usuarios=[]
            for usuario in self.get_queryset():
                data_usuario={}
                data_usuario['id']=usuario.id
                data_usuario['nombres']=usuario.nombres
                data_usuario['apellidos']=usuario.apellidos
                data_usuario['email']=usuario.email
                data_usuario['username']=usuario.username
                data_usuario['usuario_activo']=usuario.usuario_activo
                lista_usuarios.append(data_usuario)
            print(lista_usuarios)
            print(type(lista_usuarios))
            data=json.dumps(lista_usuarios)
        else:
            return render(request,self.template_name)'''
 
class RegistrarUsuario(LoginRequiredMixin,CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'users/crear_usuario.html'
   

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('accounts:inicio_usuarios')

class EditarUsuario(LoginRequiredMixin,UpdateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'users/editar_usuario.html'
    

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('usuarios:inicio_usuarios')



class EliminarUsuario(LoginRequiredMixin,DeleteView):
    model=Usuario
    template_name='users/eliminar_usuario.html'

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            usuario = self.get_object()
            usuario.usuario_activo = False
            usuario.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('accounts:inicio_usuarios')
