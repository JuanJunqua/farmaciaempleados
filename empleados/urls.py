from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='base'),
    path('busqueda/', views.empleados, name='busqueda'),
    path('encargados/', views.encargados, name='encargados'),
    path('subencargados/', views.subencargados, name='subencargados'),
    path('mostradores/', views.mostradores, name='mostradores'),
]
