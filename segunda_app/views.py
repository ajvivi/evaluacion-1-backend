from django.shortcuts import render

# Create your views here.
def vista_servicios(request):
    return render(request, 'segunda_app/servicios.html')

def vista_nosotros(request):
    return render(request, 'segunda_app/nosotros.html')