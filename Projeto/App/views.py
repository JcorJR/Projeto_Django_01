from django.shortcuts import render, redirect
from django.http import HttpResponse
# responsável por carregar, renderizar e gerenciar os arquivos HTML
from django.template import loader
#import dos formularios
from App.forms import FormUsuario, FormContato
#Import do modelo:
from App.models import Usuario,Contato
    
#====================================================================

#Crud Usuario

def editar_usuario(request, id_usuario):
    #Retorna a instância do usuário do id selecionado
    usuario = Usuario.objects.get(id=id_usuario)
    #Rentorna os dados da instancia selecionada para o form
    form = FormUsuario(request.POST or None, instance=usuario)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('appHome')
    context = {
        'form' : form
    }
    return render(request, 'editar_usuario.html', context)
        
def add_usuario(request):
    #recebe os dados do form ou o form em branco
    formUsuario = FormUsuario(request.POST or None)
    
    #se o form for postado
    if request.POST:
        #se o dados do post são válidos
        if formUsuario.is_valid():
            #Salva os dados
            formUsuario.save()
            #Retorna a home
            return redirect('appHome')
         
    #se form em branco, cira o dicionário de dados do form
    context = {
        'form' : formUsuario
    }
    
    #Renderiza o template com o form em branco
    return render(request, 'add_usuario.html', context)

#Função para excluir usuário recebendo o id como argumento
def excluir_usuario(request, id_usuario):
    #usa o id para localizar o registro correto para tabela
    usuario = Usuario.objects.get(id=id_usuario)
    
    #Deleta o registro
    usuario.delete()
    
    #Redireciona para a home.html
    return redirect('appHome')

#====================================================================
   
def appHome(request):
    #Cria um objeto com todos os valores do modelo:
    userlist = Usuario.objects.all().values()
    
    #Cria um dicionário que contem o objeto
    context = {
        'usuarios' : userlist
    }
    
    template = loader.get_template("home.html")

    #Envia o objeto para a página
    return HttpResponse(template.render(context))

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
            return redirect('appHome')
         
    #se form em branco, cria o dicionário de dados do form
    context = {
        'form' : formContato
    }
    
    #Renderiza o template com o form em branco
    return render(request, 'contato.html', context)

def listcontato(request):
    #Cria um objeto com todos os valores do modelo:
    listContato = Contato.objects.all().values()
    
    #Cria um dicionário que contem o objeto
    context = {
        'mensagens' : listContato
    }
    
    template = loader.get_template("listcontato.html")

    #Envia o objeto para a página
    return HttpResponse(template.render(context))

#Função para excluir usuário recebendo o id como argumento
def excluir_contato(request, id_contato):
    #usa o id para localizar o registro correto para tabela
    contato = Contato.objects.get(id=id_contato)
    
    #Deleta o registro
    contato.delete()
    
    #Redireciona para a home.html
    return redirect('listcontato')

#====================================================================