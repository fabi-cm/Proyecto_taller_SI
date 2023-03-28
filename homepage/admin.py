from django.contrib import admin
from .models import Proyect, Usuario, Emprendedor, Consumidor, Producto

# Register your models here.
admin.site.register(Proyect)

admin.site.register(Usuario)
admin.site.register(Emprendedor)
admin.site.register(Consumidor)
admin.site.register(Producto)