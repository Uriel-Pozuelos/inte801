from db.db import db
from sqlalchemy.orm import relationship

class MermaMateria(db.Model):
    __tablename__ = "mermas_material"
    id = db.Column(db.Integer, primary_key=True)
    idInventarioMaterias = db.Column(db.Integer, db.ForeignKey('inventario_mp.id'), nullable=False)
    merma_tipo = db.Column(db.String(200), nullable=False)
    merma_fecha = db.Column(db.DateTime, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    id_produccion = db.Column(db.Integer, db.ForeignKey('produccion.idProduccion'), nullable=True)
    justificacion = db.Column(db.Text, nullable=False)
    id_proveedor = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=True)
    
    def serialize(self):
        return {
            'id': self.id,
            'idInventarioMaterias': self.idInventarioMaterias,
            'merma_tipo': self.merma_tipo,
            'merma_fecha': self.merma_fecha,
            'cantidad': self.cantidad,
            'created_at': self.created_at,
            'id_produccion': self.id_produccion,
            'justificacion': self.justificacion,
            'id_proveedor': self.id_proveedor
        }
    