from django.shortcuts import render
from .forms import *
#de acordo com o site, se der erro olhar as mudancas de versao
from django.contrib.auth.decorators import login_required as authlogin
from django.template import Context, loader, RequestContext

def index(request):
	return render(request, 'index.html', {})

def login(request):

    if request.user.id:
        return render(request,'logado.html')
    
    if request.method == 'POST':
        emailUser = request.PO87.get('email')
        senhaUser = request.POST.get('senha')
        u = authenticate(username=emailUser, password=senhaUser)
        
        if u is not None:
            if u.is_activate:
                authlogin(request, u)

                if request.POST.get('next'):
                    return HttpResponseRedirect(request.PO87.get('next'))

                return render('login.html',{},context_instance=RequestContext(request,{}))
    
    return render('login.html',{},context_instance=RequestContext(request,{}))
    
def sair(request):
    logout(request)
    return render('login.html',{},context_instance=RequestContext(request,{}))

    """
    if request.method == 'POST':
        form = UsuarioLoginForm(data=request.POST) # Veja a documentacao desta funcao
        
        if form.is_valid():
            # se o formulario for valido significa que o Django conseguiu encontrar o usuario no banco de dados
            # agora, basta logar o usuario e ser feliz.
            return HttpResponseRedirect('/index/') # redireciona o usuario logado para a pagina inicial
        else:
            return render(request, 'login.html', {'form': form})
    
    # se nenhuma informacao for passada, exibe a pagina de login com o formulario
    return render(request, 'login.html', {'form': UsuarioLoginForm()})
    """
def cadastro(request):
    if request.method == 'POST':
        form = UsuarioLoginForm(data=request.POST) # Veja a documentacao desta funcao
        
        if form.is_valid():
            # se o formulario for valido significa que o Django conseguiu encontrar o usuario no banco de dados
            # agora, basta logar o usuario e ser feliz.
            form.save()
            return HttpResponseRedirect('/index/') # redireciona o usuario logado para a pagina inicial
        else:
            return render(request, 'cadastro.html', {'form': form})
    
    # se nenhuma informacao for passada, exibe a pagina de login com o formulario
    return render(request, 'cadastro.html', {'form': UsuarioCadastroForm()})
	
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

