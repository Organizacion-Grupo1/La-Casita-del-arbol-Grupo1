from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Evento(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    img = models.ImageField(null=True, blank=True, upload_to='img/eventos',help_text="Seleccione una imagen para mostrar")
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    publicado = models.DateTimeField(blank=True, null=True)

