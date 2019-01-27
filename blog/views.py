from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView
from .models import Foro, Post, Comentario, Categoria
from blog.forms import addPost
from django.urls import reverse_lazy

def blog(request):
    foros = Foro.objects.all()
    return render(request, "blog/blog.html", {'foros':foros})

def posts(request, foro_id):
    posts = Post.objects.filter(foro=foro_id).order_by('-created')
    return render(request, "blog/posts.html", {'posts':posts})

def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = Comentario.objects.filter(post=post_id).order_by('-created')
    return render(request, "blog/post.html", {'post':post, 'comentarios':comentarios})

def categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    return render(request, "blog/categoria.html", {'categoria':categoria})

# def addPost(request):
#     model = Post
#     return render(request, "blog/addpost.html", {'post':post})

def addPost(request):
  if request.method == "POST":
    # add to the DB
    form = addPost(request.POST)
    if form.is_valid():
        form.autor = request.user.id
        form.save()
        return HttpResponseRedirect(reverse('posts_index'))
 
  else:
    # show the form
    form = addPost(request)
  
  context = { 'form' : form }
  return render(request, 'blog/addpost.html', context)

class editPost(UpdateView):
    model = Post
    fields = ['titulo', 'descripcion', 'contenido', 'imagen', 'categorias', 'foro', 'autor']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('post', args=self.object.id)