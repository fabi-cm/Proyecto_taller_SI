from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


class Proyect(models.Model):
    tituto = CharField(max_length=100)
    descripcion = CharField(max_length=200)
    imagen = ImageField(upload_to="homepage/images/")
    url = URLField(blank=True)
