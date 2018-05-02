from django import template

register = template.Library()

@register.filter
def tipo_participante(value):
    TIPO_SELECT = {
        1: 'SOCIO',
        2: 'DAMA ROTARIA',
        3: 'ROTARACT',
        4: 'SOCIO CONYUGUE',
    }
    return TIPO_SELECT[value]