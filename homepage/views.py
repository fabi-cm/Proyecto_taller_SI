from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyect

# Create your views here.
def home(request):
    projects = Proyect.objects.all()
    return render(request,'home.html', {'projects':projects})

def index(request):
    return render(request,"index.html")

def reguistro(request):
    return render(request, "pagina_reguistro.html")

def inicio_sesion(request):
    return render(request, "inicio_sesion.html")

def about(request):
    return HttpResponse("<h1>About</h1>")