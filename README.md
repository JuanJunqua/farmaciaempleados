#farmacia

Hola que tal este es el readme de la app de "empleados" y "perfiles"
para empezar ir a http://localhost:8000/empleados

Basicamente es un simulador de un negocio donde se puede agregar los empleados que uno tiene (Encargado, Subencargado y Mostrador) donde uno se tiene que crear un usuario y logearse para poder agregar a un empleado, para buscar o para ver los empleados no hace falta estar logeado, para editarlos o eliminarlos si hace falta estar logeado y cada user puede editar sus propios empleados.Cada usuario puede editar su perfil y tambien puede agregar un avatar(dentro del dropdown).

Tambien tiene un chat entre users (dentro del dropdown) donde el usuario apreta iniciar chat > elige al destinatario y le puede mandar un mensaje ... despues va a lista de chats y puede ver los mensajes recividos y enviados.


Tiene 2 test uno por cada app la de empleados es un test de crear un encargado,subencargado y mostrador y la de perfiles es un test para crear un user

para correr los test python manage.py test perfiles y/o python manage.py test empleados





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

user = juanignacio
pw = holahola1234

Espero que le guste!!


pd: Cuando resetie el db  en algunos casos por alguna extraña razon cuando uno crea un encargado y despues un mostrador se crean con el mismo ID ..... y cuando uno va a editar el mostrador se va a editar el encargado hasta que se elmine el encargado, puse id=none para probar en cada def... funciono cuando lo cree .. corri los test (de crear empleados) y me dijo todo ok pero nose la verdad. En el DB deje 3 empleados que se pueden editar y no hay conflicto, despues cree otro mas en cada uno para probar y funciono.. una de las cosas que dijo en clase es que en el gitignore pongamos el sqlite (no lo puse por que quise probar eso del db). Si le parecio que esta mal le pido disculpas y borre el db y python manage.py makemigrations  y python manage.py migrate y se crea una nueva base de datos.

Juan  Ignacio Junqua



