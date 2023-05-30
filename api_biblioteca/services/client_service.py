from api_biblioteca.models import Cliente, db


class ClientService:
    @staticmethod
    def guardar_cliente(dni, nombre, telefono):
        nuevo_cliente = Cliente(dni=dni, nombre=nombre, telefono=telefono)
        db.session.add(nuevo_cliente)
        db.session.commit()

    @staticmethod
    def buscar_clientes(id=None, dni=None, nombre=None, telefono=None):
        query = Cliente.query

        if id:
            query = query.filter(Cliente.id.ilike(f"%{id}%"))
        if dni:
            query = query.filter(Cliente.dni.ilike(f"%{dni}%"))
        if nombre:
            query = query.filter(Cliente.nombre.ilike(f"%{nombre}%"))
        if telefono:
            query = query.filter(Cliente.telefono == telefono)

        clientes = query.all()

        return clientes

    @staticmethod
    def borrar_cliente(id):
        cliente = Cliente.query.get(id)

        if cliente:
            db.session.delete(cliente)
            db.session.commit()

            return True
        else:
            return False

    @staticmethod
    def actualizar_cliente(id, dni=None, nombre=None, telefono=None):
        cliente = Cliente.query.get(id)

        if not cliente:
            return None

        if dni:
            cliente.dni = dni
        if nombre:
            cliente.nombre = nombre
        if telefono:
            cliente.telefono = telefono

        db.session.commit()

        return cliente
