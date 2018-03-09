from django.db import models
from django.utils import timezone


class Participante(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nro_documento = models.CharField(max_length=20, unique=True)
    ciudad = models.CharField(max_length=100)
    club = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    email = models.EmailField()
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)

