# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bussola', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='avalia_local',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='avaliacao_estabelecimento',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('numero_estrelas_est', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='avaliacao_servico',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('numero_estrelas_ser', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='avaliacao_sobre_ser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('avaliacao_servico', models.ForeignKey(to='bussola.avaliacao_servico')),
            ],
        ),
        migrations.CreateModel(
            name='cadastro_contato',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('descricao', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='cidade',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='cidade_endereco',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('cidade', models.ForeignKey(to='bussola.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='comenta_sobre_est',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='comentario_estabelecimento',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('comenta_est', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='comentario_servico',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('comenta_ser', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='comentario_sobre_ser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('comentario_servico', models.ForeignKey(to='bussola.comentario_servico')),
            ],
        ),
        migrations.CreateModel(
            name='contato',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('descricao', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='endereco',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('complemento', models.CharField(max_length=45)),
                ('bairro', models.CharField(max_length=45)),
                ('numero', models.IntegerField()),
                ('rua', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='estabelecimeto',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='faz_comentario_est',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('comentario_estabelecimento', models.ForeignKey(to='bussola.comentario_estabelecimento')),
                ('endereco', models.ForeignKey(to='bussola.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='faz_comentario_ser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('comentario_servico', models.ForeignKey(to='bussola.comentario_servico')),
                ('endereco', models.ForeignKey(to='bussola.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='imagens',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('descricao_imagem', models.ImageField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='notificacao',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='realiza_avaliacao_est',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('avaliacao_estabelecimento', models.ForeignKey(to='bussola.avaliacao_estabelecimento')),
                ('endereco', models.ForeignKey(to='bussola.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='realiza_avaliacao_ser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('avaliacao_servico', models.ForeignKey(to='bussola.avaliacao_servico')),
                ('endereco', models.ForeignKey(to='bussola.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='servico',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('nome', models.CharField(max_length=45)),
                ('informacoes_adicionais', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='servico_sub_categoria',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('servico', models.ForeignKey(to='bussola.servico')),
            ],
        ),
        migrations.CreateModel(
            name='sub_categoria',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_contato',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('tipo', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('cpf_cnpj', models.IntegerField()),
                ('senha', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('nome', models.CharField(max_length=45)),
                ('foto', models.ImageField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='usuario_cadastra_ser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('servico', models.ForeignKey(to='bussola.servico')),
                ('usuario', models.ForeignKey(to='bussola.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='usuario_cidade',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('cidade', models.ForeignKey(to='bussola.cidade')),
                ('endereco', models.ForeignKey(to='bussola.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='usuario_cria_notificacao',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('notificacao', models.ForeignKey(to='bussola.notificacao')),
                ('usuario', models.ForeignKey(to='bussola.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='usuario_le_notificacao',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('notificacao', models.ForeignKey(to='bussola.notificacao')),
                ('usuario', models.ForeignKey(to='bussola.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='usuario_segue_ser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('servico', models.ForeignKey(to='bussola.servico')),
                ('usuario', models.ForeignKey(to='bussola.usuario')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='servico_sub_categoria',
            name='sub_categoria',
            field=models.ForeignKey(to='bussola.sub_categoria'),
        ),
        migrations.AddField(
            model_name='imagens',
            name='servico',
            field=models.ForeignKey(to='bussola.servico'),
        ),
        migrations.AddField(
            model_name='contato',
            name='tipo_contato',
            field=models.ForeignKey(to='bussola.tipo_contato'),
        ),
        migrations.AddField(
            model_name='comentario_sobre_ser',
            name='servico',
            field=models.ForeignKey(to='bussola.servico'),
        ),
        migrations.AddField(
            model_name='comenta_sobre_est',
            name='comentario_estabelecimento',
            field=models.ForeignKey(to='bussola.comentario_estabelecimento'),
        ),
        migrations.AddField(
            model_name='comenta_sobre_est',
            name='endereco',
            field=models.ForeignKey(to='bussola.endereco'),
        ),
        migrations.AddField(
            model_name='cidade_endereco',
            name='endereco',
            field=models.ForeignKey(to='bussola.endereco'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='sub_categoria',
            field=models.ForeignKey(to='bussola.sub_categoria'),
        ),
        migrations.AddField(
            model_name='cadastro_contato',
            name='contato',
            field=models.ForeignKey(to='bussola.contato'),
        ),
        migrations.AddField(
            model_name='cadastro_contato',
            name='endereco',
            field=models.ForeignKey(to='bussola.endereco'),
        ),
        migrations.AddField(
            model_name='avaliacao_sobre_ser',
            name='servico',
            field=models.ForeignKey(to='bussola.servico'),
        ),
        migrations.AddField(
            model_name='avalia_local',
            name='avaliacao_estabelecimento',
            field=models.ForeignKey(to='bussola.avaliacao_estabelecimento'),
        ),
        migrations.AddField(
            model_name='avalia_local',
            name='endereco',
            field=models.ForeignKey(to='bussola.endereco'),
        ),
    ]
