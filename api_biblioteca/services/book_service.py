from api_biblioteca.models import Libro, db


class BookService:
    @staticmethod
    def guardar_libro(titulo, autor, genero, año):
        nuevo_libro = Libro(titulo=titulo, autor=autor, genero=genero, año=año)
        db.session.add(nuevo_libro)
        db.session.commit()

    @staticmethod
    def buscar_libros(titulo=None, autor=None, genero=None, año=None):
        query = Libro.query

        if titulo:
            query = query.filter(Libro.titulo.ilike(f"%{titulo}%"))
        if autor:
            query = query.filter(Libro.autor.ilike(f"%{autor}%"))
        if genero:
            query = query.filter(Libro.genero.ilike(f"%{genero}%"))
        if año:
            query = query.filter(Libro.año == año)

        libros = query.all()
        return libros
