from django.shortcuts import render, redirect 
from .models import encargado, subencargado, mostrador
from .forms import EncargadoForm,SubencargadoForm,MostradorForm
from django.db.models import Q
from functools import reduce
from operator import or_


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