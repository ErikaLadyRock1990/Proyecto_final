from flask import Blueprint, jsonify, request
from .models import *
from .services.book_service import BookService
from .services.client_service import ClientService
from .services.borrow_service import BorrowService
from datetime import date

bp = Blueprint("api_biblioteca", __name__)

DIAS_DE_PRESTAMO = 31


@bp.route("/")
def index():
    return "Proyecto final"


@bp.route("/guardar-libro", methods=["POST"])
def guardar_libro():
    titulo = request.json.get("titulo")
    autor = request.json.get("autor")
    genero = request.json.get("genero")
    año = request.json.get("año")

    BookService.guardar_libro(titulo, autor, genero, año)

    return "Libro guardado correctamente", 201


@bp.route("/buscar-libro", methods=["GET"])
def buscar_libros():
    id = request.json.get("id")
    titulo = request.json.get("titulo")
    autor = request.json.get("autor")
    genero = request.json.get("genero")
    año = request.json.get("año")

    libros = BookService.buscar_libros(
        id=id, titulo=titulo, autor=autor, genero=genero, año=año
    )

    libros_json = []
    for libro in libros:
        libro_json = {
            "id": libro.id,
            "titulo": libro.titulo,
            "autor": libro.autor,
            "genero": libro.genero,
            "año": libro.año,
        }
        libros_json.append(libro_json)

    return jsonify(libros_json)


@bp.route("/borrar-libro", methods=["POST"])
def borrar_libro():
    id = request.json.get("id")  # Obtener el valor del campo "id" del JSON
    if not id:
        return jsonify({"mensaje": "Libro no encontrado"}), 400

    # Intentar borrar el libro utilizando el ID
    libro_borrado = BookService.borrar_libro(id)

    if libro_borrado:
        return jsonify({"mensaje": "Libro borrado correctamente"}), 200
    else:
        return jsonify({"mensaje": "No se encontró el libro"}), 404


@bp.route("/actualizar-libro", methods=["POST"])
def actualizar_libro():
    id = request.json.get("id")
    titulo = request.json.get("titulo")
    autor = request.json.get("autor")
    genero = request.json.get("genero")
    año = request.json.get("año")

    libro = BookService.actualizar_libro(id, titulo, autor, genero, año)

    libro_json = {
        "id": libro.id,
        "titulo": libro.titulo,
        "autor": libro.autor,
        "genero": libro.genero,
        "año": libro.año,
    }

    return jsonify(libro_json)


@bp.route("/guardar-cliente", methods=["POST"])
def guardar_cliente():
    dni = request.json.get("dni")
    nombre = request.json.get("nombre")
    telefono = request.json.get("telefono")

    ClientService.guardar_cliente(dni, nombre, telefono)

    return "Cliente guardado correctamente", 201


@bp.route("/buscar-cliente", methods=["GET"])
def buscar_clientes():
    id = request.json.get("id")
    dni = request.json.get("dni")
    nombre = request.json.get("nombre")
    telefono = request.json.get("telefono")

    clientes = ClientService.buscar_clientes(
        id=id, dni=dni, nombre=nombre, telefono=telefono
    )

    clientes_json = []
    for cliente in clientes:
        libro_json = {
            "id": cliente.id,
            "dni": cliente.dni,
            "nombre": cliente.nombre,
            "telefono": cliente.telefono,
        }
        clientes_json.append(libro_json)

    # Puedes retornar los clientes en un formato adecuado, como JSON
    return jsonify(clientes_json)


@bp.route("/borrar-cliente", methods=["POST"])
def borrar_cliente():
    id = request.json.get("id")  # Obtener el valor del campo "id" del JSON
    if not id:
        return jsonify({"mensaje": "Cliente no encontrado"}), 400

    # Intentar borrar el libro utilizando el ID
    cliente_borrado = ClientService.borrar_cliente(id)

    if cliente_borrado:
        return jsonify({"mensaje": "Cliente borrado correctamente"}), 200
    else:
        return jsonify({"mensaje": "No se encontró el cliente"}), 404


@bp.route("/actualizar-cliente", methods=["POST"])
def actualizar_cliente():
    id = request.json.get("id")
    dni = request.json.get("dni")
    nombre = request.json.get("nombre")
    telefono = request.json.get("telefono")

    cliente = ClientService.actualizar_cliente(
        id, dni=dni, nombre=nombre, telefono=telefono
    )

    cliente_json = {
        "dni": cliente.dni,
        "nombre": cliente.nombre,
        "telefono": cliente.telefono,
    }

    return jsonify(cliente_json)


@bp.route("/nuevo-prestamo", methods=["POST"])
def nuevo_prestamo():
    id_cliente = request.json.get("id_cliente")
    id_libro = request.json.get("id_libro")

    prestamo = BorrowService.nuevo_prestamo(id_cliente, id_libro)

    if not prestamo:
        return jsonify({"Error": "El libro o el cliente no están disponibles"})

    fecha_actual = date.today()
    duracion_del_prestamo = (fecha_actual - prestamo.fecha_prestamo).days

    prestamo_json = {
        "id": prestamo.id,
        "id_cliente": prestamo.id_cliente,
        "id_libro": prestamo.id_libro,
        "titulo": prestamo.titulo,
        "nombre_cliente": prestamo.nombre,
        "devuelto": prestamo.devuelto,
        "fecha_prestamo": prestamo.fecha_prestamo.strftime("%Y-%m-%d"),
        "dias_restantes": DIAS_DE_PRESTAMO - duracion_del_prestamo,
    }

    return jsonify(prestamo_json)


@bp.route("/buscar-prestamo", methods=["GET"])
def buscar_prestamos():
    dni = request.json.get("dni")

    prestamos = BorrowService.buscar_prestamo(dni)

    if not prestamos:
        return jsonify({"Error": "No hay préstamos"})

    prestamos_json = []

    for prestamo in prestamos:
        fecha_actual = date.today()
        duracion_del_prestamo = (fecha_actual - prestamo.fecha_prestamo).days
        prestamo_json = {
            "id": prestamo.id,
            "id_cliente": prestamo.id_cliente,
            "id_libro": prestamo.id_libro,
            "titulo": prestamo.titulo,
            "nombre_cliente": prestamo.nombre,
            "devuelto": prestamo.devuelto,
            "fecha_prestamo": prestamo.fecha_prestamo.strftime("%Y-%m-%d"),
            "dias_restantes": DIAS_DE_PRESTAMO - duracion_del_prestamo,
        }
        prestamos_json.append(prestamo_json)

    return jsonify(prestamos_json)


@bp.route("/borrar-prestamo", methods=["POST"])
def borrar_prestamo():
    id = request.json.get("id")

    prestamo_borrado = BorrowService.borrar_prestamo(id)

    if prestamo_borrado:
        return jsonify({"Mensaje": "Préstamo borrado con éxito"})
    else:
        return jsonify({"Mensaje": "Préstamo no encontrado"})


@bp.route("/devolver-prestamo", methods=["POST"])
def devolver_prestamo():
    id = request.json.get("id")

    prestamo_devuelto = BorrowService.devolver_prestamo(id)

    if prestamo_devuelto:
        return jsonify({"Mensaje": "El préstamo se ha devuelto correctamente"})
    else:
        return jsonify({"Mensaje": "El préstamo no ha sido encontrado"})
