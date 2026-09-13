from django.shortcuts import render

# Create your views here.
def vista_inicio(request):
    return render(request, 'primera_app/inicio.html')

def vista_contacto(request):
    return render(request, 'primera_app/contacto.html')