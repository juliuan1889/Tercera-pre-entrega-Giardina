from django.template import Context
from django.template import Template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductoForm

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def inicio(request):
    return render(request, 'index.html', {})

# def crear_producto(request):
#     if request.method == 'POST':
#         form = ProductoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # return redirect('guardado.html')  # Redirige a una página de confirmación
#     else:
#         form = ProductoForm()

#     return render(request, 'padre.html', {'form': form})

