from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='base'),
    path('busqueda/', views.empleados, name='busqueda'),
    path('encargados/', views.encargados, name='encargados'),
    path('subencargados/', views.subencargados, name='subencargados'),
    path('mostradores/', views.mostradores, name='mostradores'),
    path('mostrarempleados/', views.mostrarempleados, name='mostrarempleados'),
    path('empleados/eliminar_empleado/<int:id>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('empleados/editar_empleado/<int:id>/', views.editar_empleado, name='editar_empleado'),
]