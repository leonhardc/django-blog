from django.db import models

"""
No arquivo models.py de cada app no django está contido a declaração dos metadados do app no banco de dados configurado.

Nesse arquivo é defindo os metadados ao app categoria. No caso, um unico meetadado, descrito abaixo:
    - nome_cat: Nome da Categotia de cada post. Este campo é definido como um modulo de texto com tamanho máximo de
    50 caracteres.

"""


class Categoria(models.Model):
    nome_cat = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_cat


