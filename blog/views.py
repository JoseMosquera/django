from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Foro, Post, Comentario, Categoria
from blog.forms import PostForm, ComentarioForm
from django.urls import reverse_lazy, reverse

def blog(request):
    foros = Foro.objects.all()
    return render(request, "blog/blog.html", {'foros':foros})

def posts(request, foro_id):
    posts = Post.objects.filter(foro=foro_id).order_by('-created')
    form = PostForm
    return render(request, "blog/posts.html", {'posts':posts, 'foro_id':foro_id, 'form':form})

def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = Comentario.objects.filter(post=post_id).order_by('-created')
    form = ComentarioForm
    return render(request, "blog/post.html", {'post':post, 'comentarios':comentarios, 'form':form})

def categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    return render(request, "blog/categoria.html", {'categoria':categoria})

# class AddPost(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'blog/addpost.html'
#     success_url = '/blog'

#     def post(self, request):
#         form = self.get_form()
#         if form.is_valid():
#             form.save(request=self.request)
#             return HttpResponseRedirect(self.success_url)

class editPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/editpost.html'

    def get_success_url(self):
        return reverse_lazy('post', args=[self.object.id])

def postAdd(request, foro_id):
    if(request.method=='POST'):
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            cd=form.cleaned_data
            p_titulo=cd['titulo']
            p_descripcion=cd['descripcion']
            p_contenido=cd['contenido']
            p_imagen=cd['imagen']
            p_autor=request.user
            p_foro=Foro.objects.get(id=foro_id)
            p_categorias=cd['categorias']
            post=Post(titulo=p_titulo, descripcion=p_descripcion, contenido=p_contenido, imagen=p_imagen, autor=p_autor, foro=p_foro)
            post.save()
            post.categorias.set(p_categorias)
            return HttpResponseRedirect(reverse('posts', args=[foro_id]))
    else:
        form=PostForm()
    return render(request, 'blog/categoria.html',{'form':form})

def comentario(request, post_id):
    if(request.method=='POST'):
        form=ComentarioForm(request.POST, request.FILES)
        if form.is_valid():
            cd=form.cleaned_data
            c_contenido=cd['contenido']
            c_imagen=cd['imagen']
            c_autor=request.user
            c_post=Post.objects.get(id=post_id)
            comentario=Comentario(contenido=c_contenido, imagen=c_imagen, autor=c_autor, post=c_post)
            comentario.save()
            return HttpResponseRedirect(reverse('post', args=[post_id]))
    else:
        form=ComentarioForm()
    return render(request, 'blog/categoria.html',{'form':form})