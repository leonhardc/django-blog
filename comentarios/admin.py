from django.contrib import admin
from .models import Comentario


"""

ComentarioAdmin é a classe de configuração dos campos que serão exibidos, clicáveis e editáveis na janela admin do
app comentarios.

    - list_display: campos que serão exibidos na janela admin dos comentarios.
    - list_editable: campos que serão editáveis na janela admin dos comentarios.
    - list_display_links: campos que serão clicáveis na janela admin dos comentarios.


"""


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_comentario', 'email_comentario',
                    'usuario_comentario', 'post_comentario',
                    'data_comentario', 'publicado_comentario')

    list_editable = ('publicado_comentario',)

    list_display_links = ('id', 'nome_comentario', 'email_comentario')


# admin.register() funciona como uma forma de dizer ao django aplicar o que foi pedido eem ComentarioAdmin
admin.register(Comentario, ComentarioAdmin)


