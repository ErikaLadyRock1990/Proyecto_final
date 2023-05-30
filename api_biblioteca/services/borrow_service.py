from api_biblioteca.models import Prestamo, Libro, Cliente, db
from .book_service import BookService
from .client_service import ClientService


class BorrowService:
    @staticmethod
    def nuevo_prestamo(id_cliente, id_libro):
        clientes = ClientService.buscar_clientes(id_cliente)
        libros = BookService.buscar_libros(id_libro)

        libro_prestado = Prestamo.query.filter_by(
            id_libro=id_libro, devuelto=False
        ).first()

        if not clientes or not libros or libro_prestado:
            return None

        prestamo_nuevo = Prestamo(
            id_libro=libros[0].id,
            id_cliente=clientes[0].id,
            titulo=libros[0].titulo,
            nombre=clientes[0].nombre,
        )
        db.session.add(prestamo_nuevo)
        db.session.commit()

        prestamo = Prestamo.query.get(prestamo_nuevo.id)

        return prestamo

    @staticmethod
    def buscar_prestamo(dni):
        clientes = ClientService.buscar_clientes(None, dni, None, None)

        prestamos = None

        if len(clientes) > 0:
            prestamos = (
                Prestamo.query.join(Cliente).filter(Cliente.dni.ilike(f"%{dni}%")).all()
            )

        return prestamos

    @staticmethod
    def borrar_prestamo(id):
        prestamo = Prestamo.query.filter(Prestamo.id == id).first()

        if prestamo:
            db.session.delete(prestamo)
            db.session.commit()

            return True
        else:
            return False

    @staticmethod
    def devolver_prestamo(id):
        prestamo = Prestamo.query.filter(Prestamo.id == id).first()

        if prestamo:
            prestamo.devuelto = True
            
            db.session.commit()

            return True
        else:
            return False
