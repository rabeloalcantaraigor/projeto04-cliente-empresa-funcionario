# Generated by Django 3.2.5 on 2021-08-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('rg', models.IntegerField()),
                ('cpf', models.IntegerField()),
                ('telefone', models.IntegerField()),
                ('endereco', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_empresa', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=50)),
                ('cnpj', models.IntegerField()),
                ('quantidade_de_clientes', models.IntegerField()),
                ('segmento_da_empresa', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_funcionario', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('cpf', models.IntegerField()),
                ('rg', models.IntegerField()),
                ('tempo_de_servico', models.IntegerField()),
                ('remuneracao', models.IntegerField()),
            ],
        ),
    ]