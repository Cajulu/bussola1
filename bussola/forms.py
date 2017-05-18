# -*- codinng: utf-8 -*- 
from django.forms import ModelForm
from django import forms
from .models import *

#Neste documento são feitos os forms que serão chamados pelos htmls

class UsuarioCadastroForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = '__all__'
		widgets = {
			'nome': forms.TextInput(attrs={'class': 'form-control', 'maxlength':255}),
			'cpf_cnpj': forms.TextInput(attrs={'class': 'form-control', 'maxlength':255}),
			'email': forms.TextInput(attrs={'class': 'form-control', 'maxlength':255}),
			'senha': forms.PasswordInput(attrs={'class': 'form-control', 'maxlength':255}),
			#'foto': forms.ImageInput(attrs={'class': 'form-control', 'maxlength':255}),
		}

		error_messages = {
			'nome': {
				'required': 'Este campo é obrigatório'
			},

			'cpf_cnpj': {
				'required': 'Este campo é obrigatório'
			},
			
			'email': {
				'required': 'Este campo é obrigatório'
			},

			
			'senha': {
				'required': 'Este campo é obrigatório'
			},

		}
	#salva no BD
	def save(self, commit=True):
		user = super(UsuarioCadastroForm, self).save(commit=False)
		user.set_password()
		if commit:
			user.save()

class UsuarioLoginForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ('email', 'senha',)
		widgets = {
			'email': forms.TextInput(attrs={'class': 'form-control', 'maxlength':255}),
			'senha': forms.PasswordInput(attrs={'class': 'form-control', 'maxlength':255}),
		}

		error_messages = {
			'email': {
				'required': 'Este campo é obrigatório'
			},
			'senha': {
				'required': 'Este campo é obrigatório'
			},
		}

class NotificacaoForm(forms.ModelForm):

	class Meta:
		model = Notificacao
		fields = ('descricao',)

class CidadeForm(forms.ModelForm):

	class Meta:
		model = Cidade
		fields = ('descricao',)

class ServicoForm(forms.ModelForm):

	class Meta:
		model = Servico
		fields = '__all__'

class Sub_categoriaForm(forms.ModelForm):

	class Meta:
		model = Sub_categoria
		fields = ('descricao',)

class Comentario_servicoForm(forms.ModelForm):

	class Meta:
		model = Comentario_servico
		fields = '__all__'

class Tipo_contatoForm(forms.ModelForm):

	class Meta:
		model = Tipo_contato
		fields = ('tipo',)

class ContatoForm(forms.ModelForm):

	class Meta:
		model = Contato
		fields = '__all__'

class Avaliacao_servicoForm(forms.ModelForm):

	class Meta:
		model = Avaliacao_servico
		fields = ('numero_estrelas_ser',)

class CategoriaForm(forms.ModelForm):

	class Meta:
		model = Categoria
		fields = '__all__'

class EstabelecimetoForm(forms.ModelForm):

	class Meta:
		model = Estabelecimeto
		fields = ('nome',)

class EnderecoForm(forms.ModelForm):

	class Meta:
		model = Endereco
		fields = '__all__'

class Avaliacao_estabelecimentoForm(forms.ModelForm):

	class Meta:
		model = Avaliacao_estabelecimento
		fields = ('numero_estrelas_est',)

class Comentario_estabelecimentoForm(forms.ModelForm):

	class Meta:
		model = Comentario_estabelecimento
		fields = ('comenta_est',)

class ImagemForm(forms.ModelForm):

	class Meta:
		model = Imagens
		fields = '__all__'

class Fale_conoscoForm(forms.ModelForm):

	class Meta:
		model = Fale_conosco
		fields = '__all__'