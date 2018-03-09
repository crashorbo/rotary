from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, ListView, UpdateView
from .models import Participante
from .forms import ParticipanteForm

def index(request):
    return render(request, 'portal/index.html')


@login_required(login_url='/cuentas/login/')
def inicio(request):
    return render(request, 'portal/inicio.html')


class ParticipanteList(ListView):
    model = Participante
    template_name = 'portal/participante.html'
    context_object_name = 'participante_lista'

    def get_queryset(self, *args, **kwargs):
        return Participante.objects.filter(usuario=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParticipanteList, self).dispatch(*args, **kwargs)


class ParticipanteCreate(CreateView):
    model = Participante
    form_class = ParticipanteForm
    template_name = 'portal/participante_registro.html'
    success_url = reverse_lazy('participante')

    def form_valid(self, form):
        form.save(self.request.user)
        return super(ParticipanteCreate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParticipanteCreate, self).dispatch(*args, **kwargs)


class ParticipanteUpdate(UpdateView):
    model = Participante
    form_class = ParticipanteForm
    template_name = 'portal/participante_registro.html'
    success_url = reverse_lazy('participante')

    def form_valid(self, form):
        form.save(self.request.user)
        return super(ParticipanteUpdate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParticipanteUpdate, self).dispatch(*args, **kwargs)