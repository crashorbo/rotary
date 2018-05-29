from django.db import models
from django.utils import timezone

TIPO_CHOICES = (
    (1, 'SOCIO'),
    (2, 'DAMA ROTARIA'),
    (3, 'ROTARACT'),
    (4, 'SOCIO CONYUGUE'),
)

TIPO_ESTADO = (
    (True, 'SI'),
    (False, 'NO')
)

class Inscripcion(models.Model):
    tipo = models.IntegerField(choices=TIPO_CHOICES, default=1)
    email = models.EmailField(unique=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.BooleanField(default=False, choices=TIPO_ESTADO)
    detalle_deposito = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{} {}'.format(self.email, self.tipo)


class Participante(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE, default=None)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nro_documento = models.CharField(max_length=20, unique=True)
    ciudad = models.CharField(max_length=100)
    club = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    material = models.BooleanField(default=False, choices=TIPO_ESTADO)
    credencial = models.BooleanField(default=False, choices=TIPO_ESTADO)
    certificado = models.BooleanField(default=False, choices=TIPO_ESTADO)
    ina = models.BooleanField(default=False, choices=TIPO_ESTADO)
    pt = models.BooleanField(default=False, choices=TIPO_ESTADO)
    cg = models.BooleanField(default=False, choices=TIPO_ESTADO)
    
    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)
