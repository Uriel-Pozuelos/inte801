from db.db import db
import datetime

class Galleta_materia(db.Model):
    __tablename__ = "relacionGalletaMateria"
    idRelacion = db.Column(db.Integer, primary_key = True)
    idLoteMateria = db.Column(db.Integer, nullable=False)
    idLoteGalletas = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)


    def serialize(self):
        return {
            'idRelacion': self.idRelacion,
            'idLoteMateria': self.idLoteMateria,
            'idLoteGalletas': self.idLoteGalletas,
            'created_at': self.created_at
        }