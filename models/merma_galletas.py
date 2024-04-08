from db.db import db
import datetime

class Merma_galletas(db.Model):
    __tablename__ = "merma_galletas"
    idLoteMermas = db.Column(db.Integer, primary_key=True)
    idInventarioGalletas = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    fechaCaducidad = db.Column(db.DateTime, nullable=False)
    justificaion = db.Column(db.String, nullable=False)
    estatus = db.Column(db.String, default=1)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def serialize(self):
        return {
            'idLoteMermas': self.idLoteMermas,
            'idInventarioGalletas': self.idInventarioGalletas,
            'cantidad': self.cantidad,
            'fechaCaducidad': self.fechaCaducidad,
            'justificacion': self.justificaion,
            'estatus': self.estatus,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }