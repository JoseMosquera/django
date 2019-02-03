from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Carrera(models.Model):
    nombre = models.CharField(max_length=50, unique = True)
    distancia = models.CharField(max_length=10)
    plazas = models.CharField(max_length=5)
    participante = models.ManyToManyField(User, through='Posicion')
    created = models.DateField(auto_now_add=True, verbose_name="Fecha creacion")
    updated = models.DateField(auto_now=True, verbose_name="Fecha ultima actualizacion")

    class Meta:
        verbose_name="carrera"
        verbose_name="carreras"
        ordering=["nombre"]

    def __str__(self):
        return self.nombre+", "+self.distancia+", "+self.plazas

class Posicion(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posicion = models.CharField(max_length=2)
    created = models.DateField(auto_now_add=True, verbose_name="Fecha creacion")
    updated = models.DateField(auto_now=True, verbose_name="Fecha ultima actualizacion")

    class Meta:
        verbose_name="posicion"
        verbose_name="posiciones"
        ordering=["user"]

    def __str__(self):
        return self.carrera

class Entreno(models.Model):
    nombre = models.CharField(max_length=50, unique = True)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="carreras", default="hola")
    corredor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="corredorEntreno")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha creacion")
    updated = models.DateField(auto_now=True, verbose_name="Fecha ultima actualizacion")

    class Meta:
        verbose_name="entreno"
        verbose_name="entrenos"
        ordering=["corredor"]

    def __str__(self):
        return self.nombre