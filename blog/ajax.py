from django.http import JsonResponse

from .models import Post


def eliminar_identificador(request):
    pk = request.POST.get('identificador_id')
    identificador = Post.objects.get(pk=pk)
    identificador.delete()
    response = {}
    return JsonResponse(response)