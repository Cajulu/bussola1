from django.shortcuts import render

def index(request):
	return render(request, 'index.html', {})

def login(request):
	return render(request, 'login.html', {})

def cadastro(request):
	return render(request, 'cadastro.html', {})

def fale_conosco(request):
	return render(request, 'fale_conosco.html', {})

def estabelecimento(request):
	return render(request, 'estabelecimento', {})

def lugares(request):
	return render(request, 'lugares.html', {})

def sobre_nos(request):
	return render(request, 'sobre_nos.html', {})

def sub_categoria(request):
	return render(request, 'sub_categoria.html', {})

