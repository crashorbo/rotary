from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.template.loader import get_template
from django.core.mail import send_mail

from django.views.generic import TemplateView, FormView, ListView, UpdateView
from .forms import InscripcionForm, ParticipanteFormset, ParticipantesFormset, InscripcionUpdateForm
from .models import Inscripcion

class IndexView(TemplateView):
    template_name = 'index.html'

class AdministracionView(ListView):
    model = Inscripcion
    template_name = 'administracion/lista.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AdministracionView, self).dispatch(request, *args, **kwargs)

class InscripcionUpdateView(UpdateView):
    model = Inscripcion
    form_class = InscripcionUpdateForm
    template_name = 'administracion/update_inscripcion.html'
    success_url = reverse_lazy('administracion')

    def form_valid(self, form):
        inscripcion_email = form.cleaned_data['email']
        inscripcion_estado = form.cleaned_data['estado']
        template = get_template('administracion/confirmacion.txt')
        if (inscripcion_estado):
            send_mail(
                'Confirmacion Conferencia Rotary Distrito 4690',
                'Se le ha enviado este correo para confirmar su deposito e inscripcion a la Conferencia Distrital Rotary 4690.',
                'rotaryconfe2018@gmail.com',
                [inscripcion_email],
                fail_silently=False
            )
        return super(InscripcionUpdateView, self).form_valid(form)


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
