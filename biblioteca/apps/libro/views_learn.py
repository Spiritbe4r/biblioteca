from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.list import ListView
from .forms import AutorForm,LibroForm
from .models import Autor, Libro
from django.views.generic import View,TemplateView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

'''
class Inicio(View):

    def get(self,request,*args,**kwargs):
        return render(request,'libro/index.html')'''

class Inicio(TemplateView):
    template_name='libro/index.html'  

class ListadoAutor(ListView):
    model=Autor
    form_class=AutorForm
    template_name='libro/autor/listar_autor.html'
    #context_object_name='autores'
    queryset=Autor.objects.filter(estado=True)

    def get_queryset(self):
        
        return self.model.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        contexto={}
        contexto['autores']=self.get_queryset()
        contexto['form']=self.form_class
        
        return contexto

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect('libro:listar_autor')


    '''
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return render(self.template_name)
        else:
            return redirect('login')'''

class ActualizarAutor(UpdateView):
    model=Autor
    template_name='libro/autor/listar_autor.html'
    form_class=AutorForm
    success_url=reverse_lazy('libro:listar_autor')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autores']=Autor.objects.filter(estado=True)
        return context
'''
class CrearAutor(CreateView):
    model=Autor
    template_name='libro/autor/crear_autor.html'
    form_class=AutorForm
    success_url=reverse_lazy('libro:listar_autor')'''


class EliminarAutor(DeleteView):
    model=Autor
    

    def post(self,request,pk,*args,**kwargs):
        object=Autor.objects.get(id=pk)
        object.estado=False
        object.save()
        return redirect('libro:listar_autor')

'''
class ListadoLibros(ListView):
    model = Libro
    context_object_name = 'libros'
    template_name='libro/libro/listar_libro.html'
    queryset=Libro.objects.filter'''

class ListadoLibros(View):
    model = Libro
    form_class=LibroForm
   # context_object_name = 'libros'
    template_name='libro/libro/listar_libro.html'
    

    def get_queryset(self):
        
        return self.model.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        contexto={}
        contexto['libros']=self.get_queryset()
        contexto['form']=self.form_class
        
        return contexto

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect('libro:listar_libros')

'''
class CrearLibros(CreateView):
    model = Libro
    form_class=LibroForm
    
    template_name='libro/libro/crear_libro.html'
    success_url=reverse_lazy('libro:listar_libros')'''


class ActualizarLibro(UpdateView):
    model=Libro
    template_name='libro/libro/libro.html'
    form_class=LibroForm
    success_url=reverse_lazy('libro:listar_libros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libros']=Libro.objects.filter(estado=True)
        return context

class EliminarLibro(DeleteView):
    model=Libro
    

    def post(self,request,pk,*args,**kwargs):
        object=Libro.objects.get(id=pk)
        object.estado=False
        object.save()
        return redirect('libro:listar_libros')