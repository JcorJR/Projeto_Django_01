from django import forms
from App.models import Usuario, Contato

#formulário para o usuario
class FormUsuario(forms.ModelForm):
    class Meta:
        #modelo do fourmlário
        model = Usuario
        #campos do formulário
        fields = ('nome', 'sobrenome')
        
#formulário para o contato
class FormContato(forms.ModelForm):
    class Meta:
        #modelo do formulário
        model = Contato
        #campos do formulário
        fields = ('nome','email','assunto','mensagem')