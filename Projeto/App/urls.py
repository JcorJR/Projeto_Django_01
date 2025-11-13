from django.urls import path
from . import views

urlpatterns = [
    path('', views.appHome, name = "appHome"),
    path('excluir/<int:id_usuario>', views.excluir_usuario, name="excluir_usuario"),
    path('adicionar', views.add_usuario, name="add_usuario"),
    path('editar/<int:id_usuario>', views.editar_usuario, name="editar_usuario"),
]