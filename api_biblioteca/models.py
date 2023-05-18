import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from . import db


class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    año = db.Column(
        db.Integer, nullable=False
    )  # Corrección: Quité el argumento "5" de Integer

    def __repr__(self):
        return f"<Libro {self.id}>"


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(10), nullable=False, unique=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(
        db.Integer, nullable=False
    )  # Corrección: Quité el argumento "15" de Integer

    def __repr__(self):
        return f"<Cliente {self.id}>"


class Prestamo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_libro = db.Column(
        db.Integer, db.ForeignKey("libro.id"), nullable=False
    )  # Corrección: Cambié 'Libro.id' a 'libro.id'
    id_cliente = db.Column(
        db.Integer, db.ForeignKey("cliente.id"), nullable=False
    )  # Corrección: Cambié 'Cliente.id' a 'cliente.id'
    titulo = db.Column(db.String(100), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    fecha_prestamo = db.Column(
        db.Date, nullable=False, default=datetime.datetime.utcnow
    )  # Corrección: Añadí datetime antes de utcnow()

    cliente = relationship("Cliente", backref="prestamos")
    libro = relationship("Libro", backref="prestamos")

    def __repr__(self):
        return f"<Préstamo {self.id}>"
