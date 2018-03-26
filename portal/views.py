from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Participante, Pago
from .forms import ParticipanteForm, PagoForm

def index(request):
    return render(request, 'portal/portal.html')


@login_required
def inicio(request):
    return render(request, 'portal/inicio.html')


class ParticipanteList(ListView):
    model = Participante
    template_name = 'portal/participante.html'
    context_object_name = 'participante_lista'

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            return Participante.objects.all()
        else:
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


class ParticipanteDelete(DeleteView):
    model = Participante
    template_name = 'portal/participante_eliminar.html'
    success_url = reverse_lazy('participante')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParticipanteDelete, self).dispatch(*args, **kwargs)


class PagoList(ListView):
    model = Pago
    template_name = 'portal/pago.html'
    context_object_name = 'pago_lista'

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            return Pago.objects.all()
        else:
            return Pago.objects.filter(usuario=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PagoList, self).dispatch(*args, **kwargs)


class PagoCreate(CreateView):
    model = Pago
    form_class = PagoForm
    template_name = 'portal/pago_form.html'
    success_url = reverse_lazy('pago')

    def form_valid(self, form):
        form.save(self.request.user)
        return super(PagoCreate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PagoCreate, self).dispatch(*args, **kwargs)


class PagoUpdate(UpdateView):
    model = Pago
    form_class = PagoForm
    template_name = 'portal/pago_form.html'
    success_url = reverse_lazy('pago')

    def form_valid(self, form):
        form.save(self.request.user)
        return super(PagoUpdate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PagoUpdate, self).dispatch(*args, **kwargs)


class PagoDelete(DeleteView):
    model = Pago
    template_name = 'portal/pago_eliminar.html'
    success_url = reverse_lazy('pago')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PagoDelete, self).dispatch(*args, **kwargs)