from django.template import Context
from django.template import Template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Categoria, Marca, Producto
from .forms import ProductoFomulario

def saludo(request):
    return HttpResponse("Hola Django - Coder")

# def inicio(request):
#     return render(request, 'index.html', {})

def productoFomulario(request):

    if request.method == 'POST':
        
        miFormulario = ProductoFomulario(request.GET)
        
        print(miFormulario)
        
        producto = Producto(request.post['producto'])
        marca = Marca(request.post['marca'])
        categoria = Categoria(request.post['categoria'])
        
        producto.save()
        marca.save()
        categoria.save()
        
        return HttpResponse('exito!')
    
    return render(request, 'index.html', {})

# def crear_categoria(request):
#     if request.method == 'POST':
#         categoria_form = CategoriaForm(request.POST)
#         if categoria_form.is_valid():
#             categoria_form.save()
#             return redirect('lista_categorias')  # Redirige a la vista de lista de categorías
#     else:
#         categoria_form = CategoriaForm()
    
#     # Asegúrate de pasar el formulario correcto en el contexto de renderizado
#     return render(request, 'index.html', {'marca_form': MarcaForm(), 'categoria_form': categoria_form, 'producto_form': ProductoForm()})


