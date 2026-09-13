from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_servicios, name='servicios'),
    path('nosotros/', views.vista_nosotros, name='nosotros'),
]