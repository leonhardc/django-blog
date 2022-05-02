from django.contrib import admin
from .models import Categoria

"""
CategoriaAdmin é a classe de configuração dos campos que serão exibidos, clicáveis e editáveis na janela admin do
app categorias.

    - list_display: campos que serão exibidos na janela admin dos comentarios.
    - list_display_links: campos que serão clicáveis na janela admin dos comentarios.

"""
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cat')
    list_display_links = ('id', 'nome_cat')


# admin.register() funciona como uma forma de dizer ao django aplicar o que foi pedido eem CategoriaAdmin
admin.site.register(Categoria, CategoriaAdmin)