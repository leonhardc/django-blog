from django.urls import path
from . import views

urlpatterns = [
    path('', views, name='index'),
    path('categoria/<str:categoria>', views, name='post_categoria'),
    path('busca/', views, name='post_busca'),
    path('post/<int:pk>', views, name='post_detalhes'),
]