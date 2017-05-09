from django.db import models
from django.utils import timezone

class Notificacao(models.Model):
	descricao = models.CharField(max_length=200)
	
class Cidade(models.Model):
	descricao = models.CharField(max_length=200)

class Servico(models.Model):
	preco = models.DecimalField(max_digits=5,decimal_places=2,null=False)
	nome = models.CharField(max_length=45)
	informacoes_adicionais = models.CharField(max_length=200)

class Sub_categoria(models.Model):
	descricao = models.CharField(max_length=200)

class Comentario_servico(models.Model):
	comenta_ser =  models.CharField(max_length=200)

class Tipo_contato(models.Model):
	tipo = models.CharField(max_length=45)

class Contato(models.Model):
	tipo_contato = models.ForeignKey(Tipo_contato)
	descricao = models.CharField(max_length=45)
	
class Avaliacao_servico(models.Model):
	numero_estrelas_ser = models.IntegerField()

class Categoria(models.Model):
	sub_categoria = models.ForeignKey(Sub_categoria)
	descricao = models.CharField(max_length=45)

class Estabelecimeto(models.Model):
	nome = models.CharField(max_length=45)

class Usuario(models.Model):
	cpf_cnpj = models.IntegerField()
	senha = models.CharField(max_length=45)
	email = models.EmailField(max_length=254)
	nome = models.CharField(max_length=45)
	foto = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

class Endereco (models.Model):
	complemento = models.CharField(max_length=45)
	bairro = models.CharField(max_length=45)
	numero  = models.IntegerField()
	rua = models.CharField(max_length=45)

class Avaliacao_estabelecimento(models.Model):
	numero_estrelas_est = models.IntegerField()

class Comentario_estabelecimento(models.Model):
	comenta_est =  models.CharField(max_length=200)

class Imagens(models.Model):
	servico = models.ForeignKey(Servico)
	descricao_imagem = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

class Usuario_le_notificacao(models.Model):
	notificacao = models.ForeignKey(Notificacao)
	usuario = models.ForeignKey(Usuario)

class Usuario_segue_ser(models.Model):
	usuario = models.ForeignKey(Usuario)
	servico = models.ForeignKey(Servico)

class Usuario_cadastra_ser(models.Model):
	usuario = models.ForeignKey(Usuario)
	servico = models.ForeignKey(Servico)

class Usuario_cria_notificacao(models.Model):
	notificacao = models.ForeignKey(Notificacao)
	usuario = models.ForeignKey(Usuario)

class Cadastro_contato(models.Model):
	contato = models.ForeignKey(Contato)
	endereco = models.ForeignKey(Endereco)

class Realiza_avaliacao_ser(models.Model):
	endereco = models.ForeignKey(Endereco)
	avaliacao_servico = models.ForeignKey(Avaliacao_servico)

class Faz_comentario_ser(models.Model):
	endereco = models.ForeignKey(Endereco)
	comentario_servico = models.ForeignKey(Comentario_servico)

class Comentario_sobre_ser(models.Model):
	servico = models.ForeignKey(Servico)
	comentario_servico = models.ForeignKey(Comentario_servico)

class Avaliacao_sobre_ser(models.Model):
	servico = models.ForeignKey(Servico)
	avaliacao_servico = models.ForeignKey(Avaliacao_servico)

class Cidade_endereco(models.Model):
	endereco = models.ForeignKey(Endereco)
	cidade = models.ForeignKey(Cidade)

class Servico_sub_categoria(models.Model):
	servico = models.ForeignKey(Servico)
	sub_categoria = models.ForeignKey(Sub_categoria)

class Comenta_sobre_est(models.Model):
	endereco = models.ForeignKey(Endereco)
	comentario_estabelecimento = models.ForeignKey(Comentario_estabelecimento)

class Faz_comentario_est(models.Model):
	comentario_estabelecimento = models.ForeignKey(Comentario_estabelecimento)
	endereco = models.ForeignKey(Endereco)

class Realiza_avaliacao_est(models.Model):
	endereco = models.ForeignKey(Endereco)
	avaliacao_estabelecimento = models.ForeignKey(Avaliacao_estabelecimento)

class Avalia_local(models.Model):
	endereco = models.ForeignKey(Endereco)
	avaliacao_estabelecimento = models.ForeignKey(Avaliacao_estabelecimento)

class Usuario_cidade(models.Model):
	endereco = models.ForeignKey(Endereco)
	cidade = models.ForeignKey(Cidade)
	