from django.contrib import admin
from .models import Foro, Post, Comentario, Categoria

class ForoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    ordering = ('nombre',)
    search_fields = ('nombre',)
    date_hierarchy = 'created'

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('titulo', 'autor', 'foro', 'publicacion')
    ordering = ('autor', 'publicacion')
    search_fields = ('titulo', 'autor__username')
    date_hierarchy = 'publicacion'
    list_filter = ('autor__username', 'categorias__nombre')

class ComentarioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('contenido', 'autor', 'post', 'publicacion')
    ordering = ('autor', 'publicacion')
    search_fields = ('contenido', 'autor__username', 'post__name')
    date_hierarchy = 'publicacion'
    list_filter = ('autor__username', 'post__titulo')

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    ordering = ('nombre',)
    search_fields = ('nombre',)

admin.site.register(Foro, ForoAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Categoria, CategoriaAdmin)