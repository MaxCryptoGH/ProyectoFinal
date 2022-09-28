from importlib.metadata import requires
from django.shortcuts import render

from blogapp.models import formArticulo
from blogapp.forms import crearArticulo

# Create your views here.


def inicio(request):
    return render(request, "blogapp/inicio.html")


def media(request):
    pass


def about(request):
    return render(request, "blogapp/about.html")

# formulario para crear artículo


def articulo(request):
    if request.method == 'POST':
        forma = crearArticulo(request.POST)

        if forma.is_valid():
            data = forma.cleaned_data
            art = formArticulo(titulo=data['titulo'],
                               creador=data['creador'],
                               fecha=data['fecha'],
                               contenido=data['contenido'])
            art.save()
            return render(request, "blogapp/blog.html", {'exitoso': True})
    else:
        forma = crearArticulo()
    return render(request, "blogapp/crear_articulo.html", {"crear_articulo": forma})


# View para mostrar el artículo
def mostrarArticulo(request):
    listas = formArticulo.objects.all()
    return render(request, "blogapp/blog.html", {"listas": listas})
