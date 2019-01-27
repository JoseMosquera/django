from django.urls import path
from . import views
from .views import addPost, editPost

urlpatterns = [
    path('', views.blog, name="blog"),
    path('posts/<int:foro_id>/', views.posts, name="posts"),
    path('post/<int:post_id>/', views.post, name="post"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
    path('addpost/', views.addPost, name='addpost'),
    path('editpost/', editPost.as_view(), name='editpost')
]