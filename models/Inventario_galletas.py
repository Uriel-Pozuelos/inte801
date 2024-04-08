from db.db import db
import datetime

class Inventario_galletas(db.Model):
    __tablename__ = "inventarioGalletas"
    idLoteGalletas = db.Column(db.Integer, primary_key=True)
    idGalleta = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable = False)
    estatus = db.Column(db.Boolean, default=0, nullable = False)
    fechaCaducidad = db.Column(db.DateTime, nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable = True)


    def serialize(self):
        return {
            'idLoteGalletas': self.idLoteGalletas,
            'idGalleta': self.idGalleta,
            'cantidad': self.cantidad,
            'estatus': self.estatus,
            'fechaCaducidad': self.fechaCaducidad,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }