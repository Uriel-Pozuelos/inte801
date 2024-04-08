from db.db import db
import datetime

class solicitud_produccion(db.Model):
    __tablename__ = "solicitudproduccion"
    idSolicitud = db.Column(db.Integer, primary_key=True)
    idLoteGalletas = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable = False)
    estatus = db.Column(db.String(50), default='Pendiente')
    justificacion = db.Column(db.Text, nullable = True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now)


    def serialize(self):
        return {
            'idSolicitud': self.idSolicitud,
            'idLoteGalletas': self.idLoteGalletas,
            'cantidad': self.cantidad,
            'estatus': self.estatus,
            'justificacion': self.justificacion,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }