from django.shortcuts import render, redirect 
from .models import encargado, subencargado, mostrador
from .forms import EncargadoForm,SubencargadoForm,MostradorForm
from django.db.models import Q
from functools import reduce
from operator import or_
from django.contrib.auth.decorators import login_required

from django.http import Http404


def index(request):
    return render(request, 'base.html')

def encargados(request):
    if request.method == 'POST':
        form = EncargadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('encargados') 
    else:
        form = EncargadoForm()
    
    encargados = encargado.objects.all()
    
    return render(request, 'encargados.html', {'encargados': encargados, 'form': form})

def subencargados(request):
    if request.method == 'POST':
        form = SubencargadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subencargados')  
    else:
        form = SubencargadoForm()

    subencargados = subencargado.objects.all()

    return render(request, 'subencargados.html', {'subencargados': subencargados, 'form': form})

def mostradores(request):
    if request.method == 'POST':
        form = MostradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostradores')
    else:
        form = MostradorForm()

    mostradores = mostrador.objects.all()

    return render(request, 'mostradores.html', {'mostradores': mostradores, 'form': form})


def empleados(request):
    query = request.POST.get("busqueda") or request.GET.get("q")
    
    if query:
        encargados_result = encargado.objects.filter(
            Q(Nombre__icontains=query) | Q(Apellido__icontains=query) | Q(empleo__icontains=query) |
            reduce(or_, [Q(Nombre__icontains=word) for word in query.split()]) |
            reduce(or_, [Q(Apellido__icontains=word) for word in query.split()])
        )
        subencargados_result = subencargado.objects.filter(
            Q(Nombre__icontains=query) | Q(Apellido__icontains=query) | Q(empleo__icontains=query) |
            reduce(or_, [Q(Nombre__icontains=word) for word in query.split()]) |
            reduce(or_, [Q(Apellido__icontains=word) for word in query.split()])
        )
        mostradores_result = mostrador.objects.filter(
            Q(Nombre__icontains=query) | Q(Apellido__icontains=query) | Q(empleo__icontains=query) |
            reduce(or_, [Q(Nombre__icontains=word) for word in query.split()]) |
            reduce(or_, [Q(Apellido__icontains=word) for word in query.split()])
        )

        empleados = list(encargados_result) + list(subencargados_result) + list(mostradores_result)
    else:
        empleados = []

    return render(request, 'busqueda.html', {'empleados': empleados, 'query': query})


def mostrarempleados(request):
    encargados = encargado.objects.all()
    subencargados = subencargado.objects.all()
    mostradores = mostrador.objects.all()

    context = {
        'encargados': encargados,
        'subencargados': subencargados,
        'mostradores': mostradores,
    }

    return render(request, 'mostrarempleados.html', context)



def eliminar_empleado(request, id):
    empleado_eliminar = (
        encargado.objects.filter(id=id).first() or
        subencargado.objects.filter(id=id).first() or
        mostrador.objects.filter(id=id).first()
    )

    if request.method == "POST":
        if empleado_eliminar:
            empleado_eliminar.delete()
            return redirect('mostrarempleados')

    return render(request, 'eliminar_empleado.html', {'empleado': empleado_eliminar})

def editar_empleado(request, id):
   
    empleadoeditar = (
        encargado.objects.filter(id=id).first() or
        subencargado.objects.filter(id=id).first() or
        mostrador.objects.filter(id=id).first()
    )

    
    formularioseditar = {
        encargado: EncargadoForm,
        subencargado: SubencargadoForm,
        mostrador: MostradorForm,
    }

    if request.method == "POST":
        formulario = formularioseditar[type(empleadoeditar)](request.POST, instance=empleadoeditar)

        if formulario.is_valid():
            formulario.save()
            return redirect('mostrarempleados')
    else:
        formulario = formularioseditar[type(empleadoeditar)](instance=empleadoeditar)

    return render(request, 'editar_empleado.html', {'form': formulario, 'empleado': empleadoeditar})



