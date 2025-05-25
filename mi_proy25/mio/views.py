from django.shortcuts import render, HttpResponse
from datetime import datetime, date

# Create your views here.
def milista(request):
    nom = "marcelo aruquipa"
    fecha = date.today()
    return render(request, 'pagina.html', {'nom':nom,'fecha':fecha})