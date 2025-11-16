from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from urllib.request import urlopen
#import para a api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import DesenvolvedorSerializer
#responsável por carregar, renderizar e gerenciar os arquivos HTML
from django.template import loader
#import dos formularios
from App.forms import FormUsuario, FormContato, FormDesenvolvedor,FormCategoria,FormProduto
#Import do modelo:
from App.models import Desenvolvedor,Contato,Produto
def index(request):
    return render(request, 'index.html')
   
def sobre(request):
    return render(request, 'sobre.html')

#====================================================================

#Crud Usuario

def salvarUsuario(request):
    formulario = FormUsuario(request.POST or None)
    if request.POST:
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    return render(request, "salvar_usuario.html", {'form':formulario})
            
def loginUsuario(request):
    if request.POST:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        usuario = authenticate(request, username=nome, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('dashboard')
        else:
            messages.error(request, "Usuário ou senha incorretos")
    return render(request, "login.html")

def logoutUsuario(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def dashboard(request):
    if not request.user:
        return redirect('login')
    return render(request, "dashboard.html", {'usuario':request.user})
#====================================================================

#API

#Define que esta função é uma view de API que só responde a solicitações GET
@api_view(['GET', 'POST'])
#Função que aceita uma solicitação HTTP Django como argumento
def getApiDev(request):
    if request.method =='GET':
        desenvolvedores = Desenvolvedor.objects.all()
        serializer = DesenvolvedorSerializer(desenvolvedores, many=True)
        return Response(serializer.data)
    #Verifica se a solicitação HTTP é do tipo POST
    elif request.method == 'POST':
        #Inicializa um serializador com os dados da solicitação POST
        serializer = DesenvolvedorSerializer(data=request.data)
        #Verifica se os dados são válidos de acordo como serializer
        if serializer.is_valid():
            #salva os dados no banco de dados
            serializer.save()
            #Retorna uma resposta HTTP com os dados salvos e o status criado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #Retorna uma resposta HTTP com os erros de validação, se houveram
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def getIdApiDev(request, id_dev):
    try:
        desenvolvedor = Desenvolvedor.objects.get(id = id_dev)
    except Desenvolvedor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DesenvolvedorSerializer(desenvolvedor)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        desenvolvedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = DesenvolvedorSerializer(desenvolvedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_api(request):
    url = 'https://fakestoreapi.com/products'
    response = urlopen(url)
    dados = json.loads(response.read())
    return render(request, 'api.html', {'dadosapi':dados})

#====================================================================

# Crud desenvolverdores

def dev(request):
    devs = Desenvolvedor.objects.all().values()
    return render(request, 'desenvolvedores.html', {'desenvolvedores':devs})

def excluirDev(request, id_dev):
    dev = Desenvolvedor.objects.get(id=id_dev)
    dev.delete()
    return redirect('dev')

def salvarDev(request):
    formulario = FormDesenvolvedor(request.POST or None)
    if request.POST:
        if formulario.is_valid():
            formulario.save()
            return redirect('dev')

    return render(request, 'salvardev.html',{'form':formulario})

def editarDev(request, id_dev):
    dev = Desenvolvedor.objects.get(id=id_dev)
    formulario = FormDesenvolvedor(request.POST or None, instance=dev)
    if request.POST:
        if formulario.is_valid():
            formulario.save
            return redirect('dev')
    return render(request, 'editardev.html',{'form':formulario})

#====================================================================

#Crud Contato

def contato(request):
    #recebe os dados do form ou o form em branco
    formContato = FormContato(request.POST or None)
    
    #se o form for postado
    if request.POST:
        #se o dados do post são válidos
        if formContato.is_valid():
            #Salva os dados
            formContato.save()
            #Retorna a home
            return redirect('index')
         
    #se form em branco, cria o dicionário de dados do form
    context = {
        'form' : formContato
    }
    
    #Renderiza o template com o form em branco
    return render(request, 'contato.html', context)

def listcontato(request):
    #Cria um objeto com todos os valores do modelo:
    listContato = Contato.objects.all().values()
    return render(request, 'listcontato.html', {'contato':listContato})

#Função para excluir usuário recebendo o id como argumento
def excluir_contato(request, id_contato):
    #usa o id para localizar o registro correto para tabela
    contato = Contato.objects.get(id=id_contato)
    
    #Deleta o registro
    contato.delete()
    
    #Redireciona para a home.html
    return redirect('listcontato')

#====================================================================

#Crud Produto

def Produtos(request):
    produto = Produto.objects.all()
    return render(request, 'produtos.html', {'prods':produto})

def salvar_produtos(request,id_prod):
    if request.POST:
        formulario = FormProduto(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = FormProduto()
    return render(request, 'salvar_produtos.html', {'form':formulario})
#====================================================================