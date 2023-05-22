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

    @staticmethod
    def borrar_libro(id):
        libro = Libro.query.get(id)  # Buscar el libro por su ID

        if libro:
            db.session.delete(libro)  # Eliminar el libro de la base de datos
            db.session.commit()  # Confirmar los cambios en la base de datos
            return True  # Indicar que se borró el libro con éxito
        else:
            return False  # Indicar que no se encontró el libro con el ID especificado

    @staticmethod
    def actualizar_libro(id, titulo=None, autor=None, genero=None, año=None):
        libro = Libro.query.get(id)  # Buscar el libro por su ID

        if not libro:
            return None  # Devolver None si no se encuentra el libro

        if titulo:
            libro.titulo = titulo
        if autor:
            libro.autor = autor
        if genero:
            libro.genero = genero
        if año:
            libro.año = año

        db.session.commit()  # Confirmar los cambios en la base de datos

        return libro  # Devolver el libro actualizado
