from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


class Proyect(models.Model):
    titulo = CharField(max_length=100)
    descripcion = CharField(max_length=200)
    imagen = ImageField(upload_to="homepage/images/")
    url = URLField(blank=True)

class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=200)
    NIT = models.IntegerField(max_length=10)
    password = models.CharField(max_length=100)
    correo = models.EmailField()
    numero_telefono: models.IntegerField(max_length=10)
    numero_cuenta_bancaria: models.IntegerField(max_length=100)
    banco = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre_completo

class Emprendedor(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_representante = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    rubro = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    imagen_perfil = models.ImageField(upload_to="Emprendedor/img_perfil/")
    # Historial ventas
    # Lista de productos
    def __str__(self) -> str:
        return self.nombre_representante

class Consumidor(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    imagen_perfil = models.ImageField(upload_to="Consumidor/img_perfil/")

    def __str__(self) -> str:
        return self.usuario.nombre_completo

class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    precio = models.IntegerField(max_length=10)
    descuento = models.IntegerField(max_length=10)

    def __str__(self) -> str:
        return self.nombre   