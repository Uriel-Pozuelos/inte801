from db.db import db
from sqlalchemy.orm import relationship

class InventarioMP(db.Model):
    __tablename__ = "inventario_mp"
    id = db.Column(db.Integer, primary_key=True)
    id_materia_prima = db.Column(db.Integer, db.ForeignKey('materiaprima.id'), nullable=False)
    cantidad = db.Column(db.String(200), nullable=False)
    idCompra = db.Column(db.Integer, db.ForeignKey('compras.id'), nullable=False)
    caducidad = db.Column(db.DateTime, nullable=False)
    estatus = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'id_materia_prima': self.id_materia_prima,
            'cantidad': self.cantidad,
            'idCompra': self.idCompra,
            'caducidad': self.caducidad,
            'estatus': self.estatus,
            'created_at': self.created_at,
        }