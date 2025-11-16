from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('sobre', views.sobre, name='sobre'),
        
    #Desenvolvedor
    path('desenvolvedor', views.dev, name='dev'),
    path('salvar_dev', views.salvarDev, name='salvar_Dev'),
    path('editar_dev/<int:id_dev>', views.editarDev, name='editar_dev'),
    path('excluir_dev?<int:id_dev>', views.excluirDev, name='excluir_dev'),
    
    #Usuario
    path('salvar_usuario', views.salvarUsuario, name='salvarUsuario'),
    path('login', views.loginUsuario, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logoutUsuario, name='logoutUsuario'),
    
    #API
    path('api_desenvolvedor', views.getApiDev, name='getApiDev'),
    path('api_desenvolvedor/<int:id_dev>', views.getIdApiDev, name='getIdApiDev'),
    path('api', views.get_api, name='getApi'),
    
    #contato
    path('contato', views.contato, name='contato'),
    path('excluir_contato/<int:id_contato>', views.excluir_contato, name="excluir_contato"),
    path('listcontato', views.listcontato,name='listcontato'),
    
    #Produtos
    path('salvar_produto', views.salvar_produtos, name='salvar_produto'),
    path('produtos',views.Produtos, name='Produtos'),

]