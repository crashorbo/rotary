from django.db import models
from django.utils import timezone

TIPO_CHOICES = (
    (1, ''),
    (2, 'DOLARES'),
)



class Participante(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nro_documento = models.CharField(max_length=20, unique=True)
    ciudad = models.CharField(max_length=100)
    club = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    email = models.EmailField()
    created_date = models.DateTimeField(default=timezone.now)
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    detalle_deposito = models.TextField(blank=True)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)

class Inscripcion(models.Model):
    tipo = models.CharField(max_length=100)