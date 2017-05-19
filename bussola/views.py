from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse
from bussola.models import Usuario

def index(request):
	return render(request, 'index.html', {})

def do_login(request):
    if request.method == 'POST':
        user=authenticate(email=request.POST['email'], senha=request.POST['senha'])
        if user is not None:
            login(request, user)
            return redirect('/index/')
    return render(request, 'login.html')

def do_logout(request):
    logout(request)
    return render('/index/')


def cadastro(request):
    form = UsuarioCadastroForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            cpf_cnpj = form.cleaned_data['cpf_cnpj']
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            foto = form.cleaned_data['foto']
            usuario = Usuario.objects.create(cpf_cnpj=cpf_cnpj, nome=nome, email=email, senha=senha, foto=foto)
            print(usuario)
            usuario.save()
            return redirect('/index/')
            #return HttpResponseRedirect(request_POST.get('next')) 
    return render(request, 'cadastro.html', context)




def estabelecimento(request):
	return render(request, 'estabelecimento.html', {})

def lugares(request):
	return render(request, 'lugares.html', {})



