#farmacia

Hola que tal este es el readme de la app de "empleados" y "perfiles"

Basicamente es un simulador de un negocio donde se puede agregar los empleados que uno tiene (Encargado, Subencargado y Mostrador) donde uno se tiene que crear un usuario y logearse para poder agregar a un empleado, para buscar o para ver los empleados no hace falta estar logeado, para editarlos o eliminarlos si hace falta estar logeado y cada user puede editar sus propios empleados.Cada usuario puede editar su perfil y tambien puede agregar un avatar(dentro del dropdown).

Tambien tiene un chat entre users (dentro del dropdown) donde el usuario apreta iniciar chat > elige al destinatario y le puede mandar un mensaje ... despues va a lista de chats y puede ver los mensajes recividos y enviados.


Tiene 2 test uno por cada app la de empleados es un test de crear un encargado y la de perfiles es un test para crear un user

Los views de empleados son ...

def encargados mostrador y subencargados (donde se crean los empleados tiene login required )
def empleados (que es el buscador)
def mostrarempleados (que es el mostrar todos )
def eliminar_empleado
def editar_empleado
def about_me (pagina de about)
def chat
def lista_chats


los views de perfiles son 

def login_view registro y agregar_avatar


tiene un base.html que basicamente lo usan todos los html del proyecto


La base de datos esta completamente vacia... solamente paso el user y pw del admin con fines academicos.
El super user puede elminar agregar users y tambien empleados 

Espero que le guste!!

Juan  Ignacio Junqua



