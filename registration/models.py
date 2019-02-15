from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(verbose_name="Imagen de avatar", upload_to='perfiles', null=True, blank=True)
    bio = models.TextField(verbose_name="Biografia", null=True, blank=True)