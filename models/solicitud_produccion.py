from db.db import db
import datetime

class solicitud_produccion(db.Model):
    __tablename__ = "solicitudProduccion"
    idSolicitud = db.Column(db.Integer, primary_key=True)
    idGalleta = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable = False)
    estatus = db.Column(db.String, default='Pendiente')
    justificacion = db.Column(db.String, nullable = True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable = True)


    def serialize(self):
        return {
            'idSolicitud': self.idSolicitud,
            'idGalleta': self.idGalleta,
            'cantidad': self.cantidad,
            'estatus': self.estatus,
            'justificacion': self.justificacion,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }