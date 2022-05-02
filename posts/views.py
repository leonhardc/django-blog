from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView


# implementando Views por Classes
class PostIndex(ListView):
    pass


class PostBusca(PostIndex):
    pass


class PostCategoria(PostIndex):
    pass


class PostDetalhes(UpdateView):
    pass



