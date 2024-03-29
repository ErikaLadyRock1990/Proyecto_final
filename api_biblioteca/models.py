import datetime
from sqlalchemy.orm import relationship
from . import db


class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    año = db.Column(db.Integer, nullable=False)
    
    prestamos_libro = relationship("Prestamo", back_populates="libro", cascade="all, delete")

    def __repr__(self):
        return f"<Libro {self.id}>"


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(10), nullable=False, unique=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    
    prestamos_cliente = relationship("Prestamo", back_populates="cliente", cascade="all, delete")

    def __repr__(self):
        return f"<Cliente {self.id}>"


class Prestamo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_libro = db.Column(db.Integer, db.ForeignKey("libro.id"), nullable=False)
    id_cliente = db.Column(db.Integer, db.ForeignKey("cliente.id"), nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    devuelto = db.Column(db.Boolean, nullable=False, default=False)
    fecha_prestamo = db.Column(
        db.Date, nullable=False, default=datetime.datetime.utcnow
    )

    libro = relationship("Libro", back_populates="prestamos_libro")
    cliente = relationship("Cliente", back_populates="prestamos_cliente")

    def __repr__(self):
        return f"<Préstamo {self.id}>"
