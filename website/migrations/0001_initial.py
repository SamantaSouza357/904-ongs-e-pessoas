# Generated by Django 2.2.4 on 2019-08-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=50, verbose_name='Sobrenome')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('email', models.CharField(max_length=255, unique=True, verbose_name='E-mail')),
                ('str_cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('str_numero', models.CharField(max_length=5, verbose_name='Número Res.')),
                ('complemento', models.CharField(max_length=255, verbose_name='Complemento')),
                ('genero', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outros')], max_length=255, verbose_name='Gênero')),
                ('telefone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Telefone')),
                ('celular', models.CharField(max_length=255, verbose_name='Celular')),
                ('motivo', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
