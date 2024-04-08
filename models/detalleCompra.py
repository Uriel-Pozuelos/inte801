from db.db import db

class DetalleCompra(db.Model):
    __tablename__ = "detalle_compra"
    id = db.Column(db.Integer, primary_key=True)
    id_compra = db.Column(db.Integer, db.ForeignKey("compras.id"), nullable=False)
    id_materia = db.Column(db.Integer, db.ForeignKey("materiaprima.id"), nullable=False)
    precio_materia = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(100), nullable=False)
    caducidad = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'id_compra': self.id_compra,
            'id_materia': self.id_materia,
            'precio_materia': self.precio_materia,
            'cantidad': self.cantidad,
            'tipo': self.tipo,
            'caducidad': self.caducidad,
            'created_at': self.created_at
        }