from django.db import models
from django.contrib.auth.models import User

class Contacto(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    asunto = models.CharField(max_length=200, verbose_name="Asunto")
    mensaje = models.TextField(verbose_name="Mensaje")