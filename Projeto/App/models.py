from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    
class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    assunto = models.CharField(max_length=101)
    mensagem = models.CharField(max_length=1024)
    

    
    
    
    