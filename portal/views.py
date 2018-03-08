from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'portal/index.html')


@login_required(login_url='/login/')
def inicio(request):
    return render(request, 'portal/inicio.html')
