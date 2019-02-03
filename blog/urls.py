from django.urls import path
from . import views
from .views import editPost

urlpatterns = [
    path('', views.blog, name="blog"),
    #Path de post
    path('posts/<int:foro_id>/', views.posts, name="posts"),
    path('post/<int:post_id>/', views.post, name="post"),
    path('addpost/<int:foro_id>', views.postAdd, name='addpost'),
    path('editpost/<int:pk>', editPost.as_view(), name='editpost'),

    #Path de categoria
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),

    #Path de comentario
    path('post/<int:post_id>', views.comentario , name='addcomentario'),
]