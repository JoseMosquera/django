from django.db import models
from ckeditor.fields import RichTextField

class Noticia(models.Model):
    titulo = models.CharField(max_length=50, verbose_name="Titulo")
    contenido = RichTextField(verbose_name="Contenido")
    descripcion = RichTextField(verbose_name="Descripcion")
    imagen = models.ImageField(verbose_name="Imagen", upload_to='noticias', null=True, blank=True)
    created = models.DateField(verbose_name="Fecha creacion", auto_now_add=True)
    updated = models.DateField(verbose_name="Fecha ultima actualizacion", auto_now=True)

    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering = ['-created']

    def __str__(self):
        return self.titulo