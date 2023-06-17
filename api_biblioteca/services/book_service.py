from api_biblioteca.models import Libro, db


class BookService:
    @staticmethod
    def guardar_libro(titulo, autor, genero, año):
        nuevo_libro = Libro(titulo=titulo, autor=autor, genero=genero, año=año)
        db.session.add(nuevo_libro)
        db.session.commit()

    @staticmethod
    def buscar_libros(id=None, titulo=None, autor=None, genero=None, año=None):
        query = Libro.query

        if id:
            query = query.filter(Libro.id.ilike(f"%{id}%"))
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

    @staticmethod
    def borrar_libro(id):
        libro = Libro.query.get(id)
        if libro:
            db.session.delete(libro)
            db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def actualizar_libro(id, titulo=None, autor=None, genero=None, año=None):
        libro = Libro.query.filter_by(id=id).first()

        if not libro:
            return None

        if titulo:
            libro.titulo = titulo
        if autor:
            libro.autor = autor
        if genero:
            libro.genero = genero
        if año:
            libro.año = año

        db.session.commit()

        return libro
