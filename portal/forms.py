from django.forms.models import inlineformset_factory
from django import forms
from .models import Inscripcion, Participante

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ('email', 'detalle_deposito')
        labels = {
            'email': 'Email',
            'detalle_deposito': 'Detalle del Deposito'}
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'detalle_deposito': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class InscripcionUpdateForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ('tipo','email', 'monto','detalle_deposito', 'estado')
        labels = {
            'tipo': 'Tipo de Inscripcion',
            'email': 'Email',
            'monto': 'Monto',
            'detalle_deposito': 'Detalle del Deposito',
            'estado': 'Confirmado',}
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
            'detalle_deposito': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = ('nombres', 'apellidos', 'nro_documento', 'ciudad', 'club', 'telefono', 'credencial', 'certificado', 'material')
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'nro_documento': 'Numero Documento de Identidad',
            'ciudad': 'Ciudad',
            'club': 'Club Rotario al que pertenece',
            'telefono': 'Telefono',
            'credencial': 'Credencial',
            'certificado': 'Certificado',
            'material': 'Material'
        }
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'nro_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'club': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'credencial': forms.Select(attrs={'class': 'form-control'}),
            'certificado': forms.Select(attrs={'class': 'form-control'}),
            'material': forms.Select(attrs={'class': 'form-control'})
        }


ParticipanteFormset = inlineformset_factory(Inscripcion,
                                            Participante,
                                            ParticipanteForm,
                                            can_delete=False,
                                            extra=1)

ParticipantesFormset = inlineformset_factory(Inscripcion,
                                             Participante,
                                             ParticipanteForm,
                                             can_delete=False,
                                             extra=2)


