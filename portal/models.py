from django.db import models
from django.utils import timezone

MONEDA_CHOICES = (
    (1, 'BOLIVIANOS'),
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
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)


class Pago(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    detalle_deposito = models.TextField()
    tipo_moneda = models.IntegerField(choices=MONEDA_CHOICES, default=1)
    validado = models.BooleanField(default=False)
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}'.format(self.monto)
