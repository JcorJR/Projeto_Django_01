from django.db import models

# Create your models here.
class Desenvolvedor(models.Model):
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=50)
    descricao = models.CharField(max_length=300)
    email = models.EmailField(unique=True) 
    
class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    assunto = models.CharField(max_length=101)
    mensagem = models.CharField(max_length=1024)

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    estoque = models.PositiveIntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.nome