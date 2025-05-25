from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.
def milista(request):
    nom = "marcelo aruquipa"
    fecha = datetime.now()
    return render(request, 'pagina.html', {'nom':nom,'fecha':fecha})