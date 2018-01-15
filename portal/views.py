from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistroForm


def index(request):
    form = RegistroForm(request.POST)
    return render(request, 'portal/index.html')


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            usuario.refresh_from_db()
            usuario.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'portal/registro.html', {'form': form})
