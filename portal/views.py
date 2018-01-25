from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect

from .forms import RegistroForm


def index(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            usuario.refresh_from_db()
            usuario.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
    else:
        form = RegistroForm()
    return render(request, 'portal/index.html', {'form': form})


def ingresar(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/portal')
                

@login_required(login_url='/login/')
def inicio(request):
    return render(request, 'portal/inicio.html')
