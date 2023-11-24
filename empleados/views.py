from django.shortcuts import render, redirect 
from .models import encargado, subencargado, mostrador
from .forms import EncargadoForm,SubencargadoForm,MostradorForm
from django.db.models import Q
from functools import reduce
from operator import or_
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from .forms import MessageForm
from django.db import models
from django.http import HttpResponseNotFound








def index(request):
    return render(request, 'base.html')

#creacion de empleados


@login_required
def encargados(request, id=None):
    if request.method == 'POST':
        form = EncargadoForm(request.POST)
        if form.is_valid():
            nuevo_encargado = form.save(commit=False)
            nuevo_encargado.creador = request.user
            nuevo_encargado.save()
            return redirect('base') 
    else:
        form = EncargadoForm(initial={'creador': request.user, 'empleo': 'encargado'})

    encargados_lista = encargado.objects.all() 
    
    return render(request, 'encargados.html', {'encargados': encargados_lista, 'form': form})




@login_required
def subencargados(request, id=None):
    if request.method == 'POST':
        form = SubencargadoForm(request.POST)
        if form.is_valid():
            nuevo_subencargado = form.save(commit=False)
            nuevo_subencargado.creador = request.user
            nuevo_subencargado.save()
            return redirect('base')  
    else:
        form = EncargadoForm(initial={'creador': request.user, 'empleo': 'subencargado'})


    subencargados_lista = subencargado.objects.all()

    return render(request, 'subencargados.html', {'subencargados': subencargados_lista, 'form': form})




@login_required
def mostradores(request, id=None):
    if request.method == 'POST':
        form = MostradorForm(request.POST)
        if form.is_valid():
            nuevo_mostrador = form.save(commit=False)
            nuevo_mostrador.creador = request.user
            nuevo_mostrador.save()
            return redirect('base')
    else:
        form = EncargadoForm(initial={'creador': request.user, 'empleo': 'mostrador'})


    mostradores_lista = mostrador.objects.all()

    return render(request, 'mostradores.html', {'mostradores': mostradores_lista, 'form': form})



#buscar
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




#ver todos los empleados
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




#eliminar
@login_required
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





#editar
@login_required
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







def about_me(request):
    return render(request, 'about.html')








#chat




@login_required
def chat(request, username):
    print(f"Usuario actual logeado: {request.user.username}")
    
    try:
        other_user = User.objects.get(username=username)
        print(f"Usuario obtenido de la base de datos: {other_user.username}")
    except User.DoesNotExist:
        print(f"El usuario {username} no existe.")
        return HttpResponseNotFound("El usuario no existe.")

    
    messages = Message.objects.filter(
        (models.Q(sender=request.user, receiver=other_user) |
         models.Q(sender=other_user, receiver=request.user))
    ).order_by('timestamp')

    if request.method == 'POST':
        form = MessageForm(request.POST, user=request.user, initial={'receiver': other_user})
        if form.is_valid():
            
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = form.cleaned_data['receiver']
            message.save()
            return redirect('chat', username=username)
    else:
        form = MessageForm(user=request.user, initial={'receiver': other_user})

    return render(request, 'chat/chat.html', {
        'other_user': other_user,
        'messages': messages,
        'form': form,
    })

@login_required
def lista_chats(request):
    current_user = request.user
    other_users = User.objects.exclude(username=current_user.username)

    last_messages = []
    for other_user in other_users:
        messages = Message.objects.filter(
            (Q(sender=current_user, receiver=other_user) |
             Q(sender=other_user, receiver=current_user))
        ).order_by('-timestamp')[:1]

        if messages:
            last_messages.append({
                'other_user': other_user,
                'content': messages[0].content,
                'sender': messages[0].sender,
                'timestamp': messages[0].timestamp,
            })

    return render(request, 'chat/lista_chats.html', {'last_messages': last_messages})