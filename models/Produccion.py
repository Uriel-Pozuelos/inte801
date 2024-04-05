from db.db import db
import datetime

class Produccion(db.Model):
    __tablename__ = "produccion"
    idProduccion = db.Column(db.Integer, primary_key=True)
    idSolicitud = db.Column(db.Integer, nullable=False)
    produccionActual = db.Column(db.Integer, default=0)
    estatus = db.Column(db.String, default='En espera')
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable = True)

    def serialize(self):
        return {
            'idProduccion': self.idProduccion,
            'idSolicitud': self.idSolicitud,
            'produccionActual': self.produccionActual,
            'estatus': self.estatus,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }