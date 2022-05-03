from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

"""

No arquivo models.py de cada app no django está contido a declaração dos metadados do app no banco de dados configurado.

No caso, o app Comentarios está contigo um model como segue a descrição:
    - id: identificador do comentario, declarado automaticamente pelo django. É um campo inteiro, Chave Primaria e 
    Não nulo, além de ser autoincrementado.
    - nome_comentario: O titulo do comentário. Definido como uma palavra de, no máximo, 150 caracteres.
    - email_comentario: Email do usuário que publicou o comentário. É declarado como um campo de email, não nulo.
    - post_comentario: O corpo do comentario. É definido como uma ForengKey com relação com Post: defalt: 'se Post for 
    excluido, seus comentários também serão.'.
    - usuario_comentario: Usuário que solicitou a publicação do comentário: Este campo é definido como uma ForegnKey com
    relação com User: defalt: "Se o usuário for excluido, não faça nada com seus posts."
    - data_comentario: Data de publicação do Post. Definido como um campo dateTimeFild com valor padrão definido na hora
    da publicação do post.
    - publicado_comentario: Campo booleano que define se o comentario será publicado ou não. defalt='Não publique.'

"""


class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=150)
    email_comentario = models.EmailField()
    comentario = models.TextField()
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_comentario = models.DateTimeField(default=timezone.now)
    publicado_comentario = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_comentario

