from django.urls import path
from .views import noticiasListView, NoticiaDetailView, AddNoticia, EditNoticia, NoticiaDelete

noticias_patterns = ([
    path('', noticiasListView.as_view(), name='noticias'),
    path('<int:pk>/', NoticiaDetailView.as_view(), name='noticia'),
    path('createnoticia/', AddNoticia.as_view(), name='addnoticia'),
    path('editnoticia/<int:pk>/', EditNoticia.as_view(), name='editnoticia'),
    path('deletenoticia/<int:pk>/', NoticiaDelete.as_view(), name='deletenoticia'),
], 'noticias')