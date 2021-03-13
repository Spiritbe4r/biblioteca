from .models import Usuario
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import CreateView, FormView
from django.views.generic import ListView
from django.contrib.auth import login,logout
from django.contrib.auth.views import LogoutView
from .forms import FormularioLogin, FormularioUsuario, UserCreationForm


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


class LogoutUsuario(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
    
class ListadoUsuario(ListView):
    model = Usuario
    template_name = "users/listar_usuario.html"

    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True)
    


class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'users/register_user.html'
    success_url=reverse_lazy('accounts:list_users')