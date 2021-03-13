from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render


from .forms import AutorForm
from .models import Autor


def Home(request):
    return render(request,'libro/index.html')
def crearAutor(request):
    if request.method=='POST':
        autor_form=AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('libro:index')
    else:
        autor_form=AutorForm()
    return render(request,'libro/crear_autor.html',{'autor_form':autor_form})

def listarAutores(request):
    autores=Autor.objects.all()
    return render(request,'libro/listar_autor.html',{'autores':autores})



def editarAutor(request,id):
    autor_form=None
    error=None

    try:
        autor=Autor.objects.get(id=id)
        if request.method=='GET':
            autor_form=AutorForm(instance=autor)
        else:
            autor_form=AutorForm(request.POST,instance=autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('libro:index')
    except ObjectDoesNotExist as e:
        error=e
    
    return render(request,'libro/crear_autor.html',{'autor_form':autor_form,'error':error})

def eliminarAutor(request,id):
    autor=Autor.objects.get(id=id)
    autor.delete()
    return redirect ('libro:listar_autor')
