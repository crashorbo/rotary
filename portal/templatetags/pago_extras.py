from django import template

register = template.Library()


@register.filter(name="estado")
def estado(valor):
    if valor:
        return "CONFIRMADO"
    else:
        return "PENDIENTE"