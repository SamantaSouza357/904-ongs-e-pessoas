from django.shortcuts import render
from website.models import Pessoa, Ong

# Create your views here.

def index(request):

    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.data_nascimento = request.POST.get('data_nascimento')
        pessoa.email = request.POST.get('email')
        pessoa.str_cep = request.POST.get('str_cep')
        pessoa.str_numero = request.POST.get('str_numero')
        pessoa.complemento = request.POST.get('complemento')
        pessoa.genero = request.POST.get('genero')
        pessoa.telefone = request.POST.get('telefone')
        pessoa.celular = request.POST.get('celular')
        pessoa.motivo = request.POST.get('motivo')
        pessoa.save()


        contexto = {
            'nome': pessoa.nome
        }
        return render(request,'index.html',contexto)

   
    return render(request, 'index.html')    

def pessoas(request):
    p =  Pessoa.objects.filter(ativo=True).all()
    contexto = {
        'pessoas' : p
    }    

    return render(request, 'pessoas.html', contexto)

def ong(request):
    if request.method == 'POST':
        ong = Ong()
        ong.nome = request.POST.get('nome_responsavel')
        ong.sobrenome = request.POST.get('cep')
        ong.data_nascimento = request.POST.get('nome_ong')
        ong.email = request.POST.get('telefone')
        ong.str_cep = request.POST.get('horario')
        ong.str_cep = request.POST.get('observacao')
        ong.save()
        
    return render(request, 'ong.html')

def cadastro_ong(request):
    o = Ong.objects.filter(ativo=True).all()
    contexto = {
        'ong': o
    }

    return render(request,'cadastro_ong',contexto)
        
    