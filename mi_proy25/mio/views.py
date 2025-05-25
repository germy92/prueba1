from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.
def milista(request):
    nom = "marcelo aruquipa"
    fecha = datetime.now()
    return render(request, 'pagina.html', {'nom':nom,'fecha':fecha})

def eliminar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)

    if publicacion.usuario != request.user:
        return HttpResponseForbidden("No puedes eliminar esta publicación.")

    if request.method == 'POST':
        publicacion.delete()
        return redirect('lista_publicaciones')

    return render(request, 'blog/confirmar_eliminacion.html', {'publicacion': publicacion})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    comentarios = Comentario.objects.filter(publicacion=publicacion)
    form_comentario = ComentarioForm() if request.user.is_authenticated else None
    contexto={
        'publicacion':publicacion,
        'comentarios':comentarios,
        'form_comentario':form_comentario,
    }
    return render(request, 'blog/detalle_publicacion.html',contexto)
