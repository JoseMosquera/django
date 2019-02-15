from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Foro(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha creacion")
    updated = models.DateField(auto_now=True, verbose_name="Fecha ultima actualizacion")

    class Meta:
        verbose_name = "foro"
        verbose_name_plural = "foros"
        ordering = ['-created']

    @property    
    def countPosts(self):
        count = self.postsForo.all().count()
        return count

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha creacion")
    updated = models.DateField(auto_now=True, verbose_name="Fecha ultima actualizacion")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Titulo")
    contenido = models.TextField(verbose_name="Contenido")
    descripcion = models.TextField(verbose_name="descripcion")
    publicacion = models.DateTimeField(verbose_name="Fecha de publicacion", default=now())
    imagen = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    autor = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE, related_name="userPost")
    foro = models.ForeignKey(Foro, on_delete=models.CASCADE, related_name="postsForo")
    categorias = models.ManyToManyField(Categoria, verbose_name="Categorias", related_name="obtener_posts")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha creacion")
    updated = models.DateField(auto_now=True, verbose_name="Fecha ultima actualizacion")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['-created']

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    contenido = models.TextField(verbose_name="Contenido")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    autor = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE)
    publicacion = models.DateTimeField(verbose_name="Fecha de publicacion", default=now())
    created = models.DateField(auto_now_add=True, verbose_name="Fecha creacion")
    updated = models.DateField(auto_now=True, verbose_name="Fecha ultima actualizacion")

    class Meta:
        verbose_name = "comentario"
        verbose_name_plural = "comentarios"
        ordering = ['-created']