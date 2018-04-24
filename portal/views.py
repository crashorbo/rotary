from django.shortcuts import render

from django.views.generic import TemplateView, FormView, ListView
from .forms import InscripcionForm, ParticipanteFormset, ParticipantesFormset
from .models import Inscripcion

class IndexView(TemplateView):
    template_name = 'index.html'

class AdministracionView(ListView):
    model = Inscripcion
    template_name = 'administracion/lista.html'
    

def create_parent(request):
    if request.method == 'POST':
        inscripcion_form = InscripcionForm(request.POST, request.FILES, prefix='inscripcion')
        participante_form = ParticipanteFormset(request.POST, request.FILES, prefix='participantes')

        inscripcion_valid = inscripcion_form.is_valid()
        participante_valid = participante_form.is_valid()

        if inscripcion_valid and participante_valid:
            inscripcion = inscripcion_form.save()
            participante_form.instance = inscripcion
            participante_form.save()
            return render(request, 'forms/form_success.html')
    else:
        inscripcion_form = InscripcionForm(prefix='inscripcion')
        participante_form = ParticipanteFormset(prefix='participantes')

    return render(request, 'forms/registro_ajax.html', {'inscripcion_form': inscripcion_form,
                                                        'participante_forms': participante_form})


def create_parents(request):
    if request.method == 'POST':
        inscripcion_form = InscripcionForm(request.POST, request.FILES, prefix='inscripcion')
        participantes_form = ParticipantesFormset(request.POST, request.FILES, prefix='participantes')

        inscripcion_valid = inscripcion_form.is_valid()
        participantes_valid = participantes_form.is_valid()

        if inscripcion_valid and participantes_valid:
            inscripcion = inscripcion_form.save()
            participantes_form.instance = inscripcion
            participantes_form.save()
            return render(request, 'forms/form_success.html')
    else:
        inscripcion_form = InscripcionForm(prefix='inscripcion')
        participantes_form = ParticipantesFormset(prefix='participantes')

    return render(request, 'forms/registros_ajax.html', {'inscripcion_form': inscripcion_form,
                                                        'participante_forms': participantes_form})
