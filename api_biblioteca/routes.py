import json
from flask import Blueprint, jsonify, request, render_template
from .models import *
from .services.book_service import BookService
from .services.client_service import ClientService
from .services.borrow_service import BorrowService
from datetime import date


bp = Blueprint("api_biblioteca", __name__)

DIAS_DE_PRESTAMO = 31


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/guardar-libro", methods=["GET", "POST"])
def guardar_libro():
    if request.method == "GET":
        return render_template("guardar_libro.html")
    
    elif request.method == "POST":
        titulo = request.form.get("titulo")
        autor = request.form.get("autor")
        genero = request.form.get("genero")
        año = request.form.get("año")

        BookService.guardar_libro(titulo, autor, genero, año)

        return jsonify({"Mensaje": "El libro se ha guardado correctamente"}), 200


@bp.route("/buscar-libros", methods=["GET", "POST"])
def buscar_libros():
    if request.method == "GET":
        return render_template("buscar_libros.html")
    
    elif request.method == "POST":
        id = request.form.get("id")
        titulo = request.form.get("titulo")
        autor = request.form.get("autor")
        genero = request.form.get("genero")
        año = request.form.get("año")

        libros = BookService.buscar_libros(
            id=id, titulo=titulo, autor=autor, genero=genero, año=año
        )

        libros_json = []

        if len(libros) == 0:
            return [], 200

        for libro in libros:
            libro_json = {
                "id": libro.id,
                "titulo": libro.titulo,
                "autor": libro.autor,
                "genero": libro.genero,
                "año": libro.año,
            }
            libros_json.append(libro_json)

        return json.dumps(libros_json)


@bp.route("/borrar-libro", methods=["POST"])
def borrar_libro():
    data = request.get_json()
    id = data.get("id")

    if not id:
        return jsonify({"Mensaje": "Libro no encontrado"}), 404

    libro_borrado = BookService.borrar_libro(id)

    if not libro_borrado:
        return jsonify({"Mensaje": "No se ha encontrado el libro o aún sigue activo el préstamo"}), 409

    return jsonify({"Mensaje": "Libro borrado correctamente"}), 200

@bp.route("/actualizar-libro", methods=["GET", "POST"])
def actualizar_libro():    
    if request.method == "GET":
        id = request.args.get("id")
        
        libros = BookService.buscar_libros(id)
        
        return render_template("actualizar_libro.html",libro=libros[0])
    
    elif request.method == "POST": 
        id = request.form.get("id")
        titulo = request.form.get("titulo")
        autor = request.form.get("autor")
        genero = request.form.get("genero")
        año = request.form.get("año")

        libro = BookService.actualizar_libro(id, titulo, autor, genero, año)

        if not libro:
            return jsonify({"Mensaje": "No se han encontrado libros"}), 404

    return jsonify({"Mensaje": "Libro actualizado"}), 200


@bp.route("/guardar-cliente", methods=["GET", "POST"])
def guardar_cliente():
    if request.method == "GET":
        return render_template("guardar_cliente.html")
    
    elif request.method == "POST":
        dni = request.form.get("dni")
        nombre = request.form.get("nombre")
        telefono = request.form.get("telefono")

        cliente = ClientService.guardar_cliente(dni, nombre, telefono)

        if cliente == "Ya existe un cliente con ese DNI":
            return jsonify({"Mensaje": cliente}), 409
        
        else:
            return jsonify({"Mensaje": "Cliente guardado correctamente"}), 200
        

@bp.route("/buscar-clientes", methods=["GET", "POST"])
def buscar_clientes():
    if request.method == "GET":
        return render_template("buscar_clientes.html")
    
    elif request.method == "POST":
        id = request.form.get("id")
        dni = request.form.get("dni")
        nombre = request.form.get("nombre")
        telefono = request.form.get("telefono")

        clientes = ClientService.buscar_clientes(
            id=id, dni=dni, nombre=nombre, telefono=telefono
        )

        clientes_json = []

        if len(clientes) == 0:
            return clientes_json, 200        

        for cliente in clientes:
            cliente_json = {
                "id": cliente.id,
                "dni": cliente.dni,
                "nombre": cliente.nombre,
                "telefono": cliente.telefono,
            }
            clientes_json.append(cliente_json)

    return json.dumps(clientes_json)


@bp.route("/borrar-cliente", methods=["POST"])
def borrar_cliente():
    id = request.json.get("id")

    cliente_borrado = ClientService.borrar_cliente(id)

    if not cliente_borrado:
        return jsonify({"Mensaje": "No se han encontrado clientes"}), 404

    return jsonify({"mensaje": "Cliente borrado correctamente"}), 200


@bp.route("/actualizar-cliente", methods=["GET", "POST"])
def actualizar_cliente():
    if request.method == "GET":
        id = request.args.get("id")
        
        clientes = ClientService.buscar_clientes(id)
        
        return render_template("actualizar_cliente.html", cliente=clientes[0])
    
    elif request.method == "POST":
        
        id = request.form.get("id")
        dni = request.form.get("dni")
        nombre = request.form.get("nombre")
        telefono = request.form.get("telefono")

        cliente = ClientService.actualizar_cliente(
            id, dni=dni, nombre=nombre, telefono=telefono
        )  

        if cliente == "No se ha encontrado el cliente":
            return jsonify({"Mensaje": cliente}), 404
        
        elif cliente == "Ya existe un cliente con ese DNI":
            return jsonify({"Mensaje": cliente}), 409
        
        else:
            return jsonify({"Mensaje": "Cliente actualizado"}), 200


@bp.route("/nuevo-prestamo", methods=["GET", "POST"])
def nuevo_prestamo():
    if request.method == "GET":
        id = request.args.get("cliente_id")
        
        clientes = ClientService.buscar_clientes(id)
        
        libros = BookService.buscar_libros(None, None, None, None, None, True)
        
        return render_template("nuevo_prestamo.html", cliente=clientes[0], libros=libros)
    
    elif request.method == "POST":
        id_cliente = request.json.get("id_cliente")
        id_libro = request.json.get("id_libro")
        
        print(id_cliente, id_libro)
        
        prestamo = BorrowService.nuevo_prestamo(id_cliente, id_libro)

        if not prestamo:
            return jsonify({"Mensaje": "El libro o el cliente no están disponibles"}), 409


        return jsonify({"Mensaje": "Préstamo guardado correctamente"}), 200


@bp.route("/buscar-prestamos", methods=["GET", "POST"])
def buscar_prestamos():    
    if request.method == "GET":
        return render_template("buscar_prestamos.html")
    
    elif request.method == "POST":
        dni = request.form.get("dni")
        
        prestamos = BorrowService.buscar_prestamos(dni)

        prestamos_json = []

        if len(prestamos) == 0:
            return prestamos_json, 200        

        for prestamo in prestamos:
            fecha_actual = date.today()
            duracion_del_prestamo = (fecha_actual - prestamo.fecha_prestamo).days
            dias_restantes = 0

            if prestamo.devuelto == False:
                dias_restantes = DIAS_DE_PRESTAMO - duracion_del_prestamo

            prestamo_json = {
                "id": prestamo.id,
                "id_cliente": prestamo.id_cliente,
                "id_libro": prestamo.id_libro,
                "titulo": prestamo.titulo,
                "nombre": prestamo.nombre,
                "devuelto": prestamo.devuelto,
                "fecha_prestamo": prestamo.fecha_prestamo.strftime("%Y-%m-%d"),
                "dias_restantes": dias_restantes,
            }
            prestamos_json.append(prestamo_json)

    return json.dumps(prestamos_json)
    

@bp.route("/borrar-prestamo", methods=["POST"])
def borrar_prestamo():
    id = request.json.get("id")

    prestamo_borrado = BorrowService.borrar_prestamo(id)

    if not prestamo_borrado:
        return jsonify({"Mensaje": "No se ha encontrado el préstamo"}), 404

    return jsonify({"Mensaje": "Préstamo borrado con éxito"}), 200


@bp.route("/devolver-prestamo", methods=["POST"])
def devolver_prestamo():
    id = request.json.get("id")

    prestamo_devuelto = BorrowService.devolver_prestamo(id)

    if not prestamo_devuelto:
        return jsonify({"Mensaje": "No se ha encontrado el préstamo"}), 404

    return jsonify({"Mensaje": "El préstamo se ha devuelto correctamente"}), 200
