from flask import Blueprint, jsonify, request
from .models import *
from .services.book_service import BookService

bp = Blueprint("api_biblioteca", __name__)


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
def buscar_libro():
    titulo = request.json.get("titulo")
    autor = request.json.get("autor")
    genero = request.json.get("genero")
    año = request.json.get("año")

    libros = BookService.buscar_libros(
        titulo=titulo, autor=autor, genero=genero, año=año
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
