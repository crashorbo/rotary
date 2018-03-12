from django import template

register = template.Library()


@register.filter(name="tipo_moneda")
def tipo_moneda(valor):
    MONEDA_CHOICES = {
        1: 'BOLIVIANOS',
        2: 'DOLARES',
    }
    return MONEDA_CHOICES[valor]


@register.filter(name="estado")
def estado(valor):
    if valor:
        return "CONFIRMADO"
    else:
        return "PENDIENTE"