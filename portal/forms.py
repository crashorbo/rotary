from django import forms

from .models import Participante


class ParticipanteForm(forms.ModelForm):

    class Meta:
        model = Participante

        fields = [
            'nombres',
            'apellidos',
            'nro_documento',
            'ciudad',
            'club',
            'telefono',
            'email',
            'created_date'
        ]

        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'nro_documento': 'Numero de Documento',
            'ciudad': 'Ciudad/Localidad',
            'club': 'Rotary Club al que pertenece',
            'telefono': 'Telefono/Movil',
            'email': 'Email',
        }

        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'nro_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'club': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'created_date': forms.HiddenInput(),
        }

    def save(self, usuario=None):
        user_profile = super(ParticipanteForm, self).save(commit=False)
        if usuario:
            user_profile.usuario = usuario
        user_profile.save()
        return user_profile

"""
class PagoForm(forms.ModelForm):

    class Meta:
        model = Pago

        fields = [
            'monto',
            'tipo_moneda',
            'detalle_deposito',
            'validado',
            'created_date',
        ]

        labels = {
            'monto': 'Monto a Pagar',
            'tipo_moneda': 'Seleccione el tipo de Moneda',
            'detalle_deposito': 'Detalle del Deposito',
        }

        widgets = {
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_moneda': forms.Select(attrs={'class': 'form-control'}),
            'detalle_deposito': forms.Textarea(attrs={'class': 'form-control'}),
            'validado': forms.HiddenInput(),
            'created_date': forms.HiddenInput(),
        }

    def save(self, usuario=None):
        user_profile = super(PagoForm, self).save(commit=False)
        if usuario:
            user_profile.usuario = usuario
        user_profile.save()
        return user_profile
"""