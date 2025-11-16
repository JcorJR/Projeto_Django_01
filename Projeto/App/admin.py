from django.contrib import admin
from .models import Categoria, Produto
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto)