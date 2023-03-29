from django.db import models


class Usuario(models.Model):
    nombre_completo = models.CharField(help_text="Introduce tu nombre completo",max_length=200)
    NIT = models.IntegerField()
    # password = models.CharField(help_text="Introduce tu contraseña", max_length=10)
    correo = models.EmailField()
    numero_telefono: models.CharField(max_length=20)
    numero_cuenta_bancaria: models.IntegerField()
    banco = models.CharField(max_length=100)
    img_perfil = models.ImageField(default="img_default.png")
    def __str__(self) -> str:
        return self.nombre_completo

class Emprendedor(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_representante = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    rubro = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    def __str__(self) -> str:
        return f"{self.usuario.nombre_completo},{self.rubro}"
    
class Perfil(models.Model):
	user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
	# image = models.ImageField(default='img_default.png')

	def __str__(self):
		return f'Perfil de {self.user.nombre_completo}'


class Producto(models.Model):
    propietario = models.ForeignKey(Emprendedor, on_delete=models.CASCADE)
