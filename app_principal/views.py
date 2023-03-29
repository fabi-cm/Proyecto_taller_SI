from django.shortcuts import render, redirect
from .forms import RegistrarUsuarioForm
from django.contrib import messages

def index(request):
    return render(request, "index.html")


def pagina_reguistro(request):
    return render(request, 'reguistro/pagina_reguistro.html')


def reguistrar_emprendedor(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['nombre_representante']
            messages.success(request, f'Usuario {username} creado')
            return redirect('index')
    else:
        form = RegistrarUsuarioForm()
    
    context = { 'form' : form }
    return render(request,"reguistro/emprendedor.html", context)

def reguistrar_producto(request):
    return render(request,"reguistro/producto.html")

