from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyect

# Create your views here.
def home(request):
    projects = Proyect.objects.all()
    return render(request,'home.html', {'projects':projects})

def about(request):
    return HttpResponse("<h1>About</h1>")