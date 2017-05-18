from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse

def index(request):
	return render(request, 'index.html', {})

def do_login(request):
    if request.method == 'POST':
        user=authenticate(email=request.POST['email'], senha=request.POST['senha'])
        if user is not None:
            login(request, user)
            return redirect('/cadastro')
        return render(request, 'bussola/login.html')

def do_logout(request):
    logout(request)
    return render('/index')


@login_required  
def cadastro(request):
    form = UsuarioCadastroForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return render(request,'/cadastro') 
    return render(request, 'bussola/cadastro.html', context)


def estabelecimento(request):
	return render(request, 'estabelecimento.html', {})

def lugares(request):
	return render(request, 'lugares.html', {})



