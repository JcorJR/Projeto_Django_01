from django.urls import path
from . import views

urlpatterns = [
    path('', views.appHome, name = "appHome"),
    #Usuario
    path('excluir_usuario/<int:id_usuario>', views.excluir_usuario, name="excluir_usuario"),
    path('adicionar', views.add_usuario, name="add_usuario"),
    path('editar_usuario/<int:id_usuario>', views.editar_usuario, name="editar_usuario"),
    #contato
    path('contato', views.contato, name='contato'),
    path('excluir_contato/<int:id_contato>', views.excluir_contato, name="excluir_contato"),
    path('listcontato', views.listcontato,name='listcontato'),
]