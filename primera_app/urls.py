from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_inicio, name='inicio'),
    path('contacto/', views.vista_contacto, name='contacto'),
]