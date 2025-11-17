from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from App.models import Desenvolvedor, Contato, Produto, Categoria, Compra


class FormDesenvolvedor(forms.ModelForm):
    class Meta:
        model = Desenvolvedor
        fields = "__all__"

#formulário de login de usuario
class FormUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
         

#formulário para o contato
class FormContato(forms.ModelForm):
    class Meta:
        #modelo do formulário
        model = Contato
        #campos do formulário
        fields = ('nome','email','assunto','mensagem')

#formulário para os produtos
class FormProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao','preco','categoria']
        
        widgets = {'nome':forms.TextInput(attrs={'placehlder':'nome do produto'}),'imagem':forms.FileInput(attrs={'accept':'imagem/*'})}
        
#formulário categoria
class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        
#formulário Compra
class FormCompra(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['quantidade']