API WEB DE UNA BIBLIOTECA
Programa hecho en python con el framework flask.
Descrición de la Api:

CRUD de clientes: Crea, lee, actualiza y elimina información de tus clientes. Puedes ver su nombre, dirección, número de teléfono y correo electrónico.

CRUD de libros: Crea, lee, actualiza y elimina información sobre los libros de la biblioteca. Puedes ver su título, autor, género, y año.

Registro de préstamos y devoluciones: Registra quién tiene prestado qué libro y cuándo debe ser devuelto.

Historial de préstamos: Obtén información acerca de los libros que ha tomado prestados un cliente en el pasado

Instalación
Crear un entorno en python que se llama "entorno_biblioteca" y ejecutar el comando
pip install -r requirements.txt
 
Ejecucion del programa
inicializar el servidor de flask
en mac: export FLASK_APP=main.py
en windows: set FLASK_APP=main.py
Otra opción de ejecucion
instalar pipi install python-dotenv
crear un archivo .env y dentro agregar lo siguiente:  FLASK_APP=main.py FLASK_DEBUG=True
y luego para lanzar seria en la terminal el comando: flask run
Comando para ejecutar el servidor:
flask --app main run

Comando para ejecutar el servidor en otro puerto diferente por default es el 5000
flask --app main run -p 5002

Comando para ejecutar el servidor en modo debug, para realizar cambios en tiempo real
flask --app main --debug run

Esta Api trabaja en formato ".json", a continuación vamos a explicar los endpoint del proyecto:


AGREGAR UN NUEVO CLIENTE
La ruta para este enpoint es la siguiente : "/guardar-cliente"
La petición para este endpoint tiene la siguiente forma:
{
	"dni": "0xxxxxxxR",
	"nombre": "Test",
	"telefono": 6xxxxxxxx
}

Esto agregará un nuevo cliente a la tabla "Crear Cliente"


BUSCAR CLIENTES
La ruta para este enpoint es la siguiente : "/buscar-clientes"
La petición para este endpoint tiene la siguiente forma:
{
    "dni": "5xxxxxxxC",
    "id": 2,
    "nombre": "Test",
    "telefono": 6xxxxxxxx
}

Esto buscará un cliente según su "id", "dni", "nombre" y/o "teléfono" en la tabla "Buscar Clientes"


BORRAR CLIENTE
La ruta para este endpoint es la siguiente : "/borrar-cliente"
La petición para este endpoint tiene la siguiente forma:
{ 
	"id": 4
}

Esto borrará el cliente con ese id asignado, en la tabla "Borrar Cliente"


ACTUALIZAR CLIENTE
La ruta para este endpoint es la siguiente : "/actualizar-cliente"
La petición para este endpoint tiene la siguiente forma:
{
	"dni": "5XXXXXXXB",
	"id": 2,
	"nombre": "Test",
	"telefono": 6xxxxxxxx
}

Se podrá modificar cualquiera de estos campos por la información correcta o nueva, quedando así actualizada en la tabla "Actualizar Cliente".El id es obligatorio y no se puede modificar.


GUARDAR LIBRO
La ruta para este endpoint es la siguiente : "/guardar-libro"
La petición para este endpoint tiene la siguiente forma:
{
	"autor": "Stephanie Meyer",
	"año": 2006,
	"genero": "Fantasía, Juvenil",
	"titulo": "Crepúsculo"
}

Esto agregará un nuevo libro a la tabla "Guardar Libro"


BUSCAR LIBROS
La ruta para este endpoint es la siguiente : "/buscar-libros"
La petición para este endpoint tiene la siguiente forma:
{
		"autor": "Stephen King",
		"año": 1986,
		"genero": "Terror",
		"id": 6,
		"titulo": "It"
}

Se puede realizar la búsqueda por cualquiera de esos campos en la tabla "Buscar Libro"


BORRAR LIBRO
La ruta para este endpoint es la siguiente : "/borrar-libro"
La petición para este endpoint tiene la siguiente forma:
{
	"id": 8
}

Esto borrará el libro con ese id asignado, en la tabla "Borrar Libro"


ACTUALIZAR LIBRO
La ruta para este endpoint es la siguiente : "/actualizar-libro"
La petición para este endpoint tiene la siguiente forma:
{
	"id": 1,
	"titulo": "Harry Potter y La Piedra Filosofal",
	"genero": "Fantasía",
	"autor": "J.K.Rowling",
	"año": 1997
}

Se podrá modificar cualquiera de estos campos por la información correcta o nueva, quedando así actualizada en la tabla "Actualizar Libro".El id es obligatorio y no puede modificarse.


AGREGAR UN NUEVO PRESTAMO
La ruta para este endpoint es la siguiente : "/nuevo-prestamo"
La petición para este endpoint tiene la siguiente forma:
{
	"id_cliente": 3,
	"id_libro": 8

}

Con estos dos datos quedará registrado el préstamo del libro, con los datos de ese cliente y durante cuántos dias se mantendrá activo, en la tabla "Nuevo Préstamo"


BUSCAR PRÉSTAMO
La ruta para este endpoint es la siguiente : "/buscar-prestamos"
La petición para este endpoint tiene la siguiente forma:
{
	"dni": "5XXXXXXXB"
}

La búsqueda sólo puede ser realizada con el dni del cliente, donde después se verá reflejada toda la información del préstamo realizado por cliente, en la tabla "Buscar Préstamo"


BORRAR PRESTAMO
La ruta para este endpoint es la siguiente : "/borrar-prestamo"
La petición para este endpoint tiene la siguiente forma:
{
	"id": 1
}

En este caso, se debe anular el préstamo con el id del mismo.


DEVOLVER PRESTAMO
La ruta para este endpoint es la siguiente : "/devolver-prestamo"
La petición para este endpoint tiene la siguiente forma:
{
	"id": 3
}

Con el id del préstamo podemos darlo por finalizado, y en la tabla "Préstamos" la columna devuelto quedará a True, quedando reflejados los datos del cliente, del libro y el contador de dias restante se quedará a cero.

