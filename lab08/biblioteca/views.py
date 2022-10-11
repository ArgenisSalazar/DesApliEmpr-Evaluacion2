from django.shortcuts import render

# Create your views here.
from .models import Libro

def all_Libro(request):
    template_name='index.html'
    libroListados=Libro.objects.all()
    return render(request,template_name,{"libros":libroListados})