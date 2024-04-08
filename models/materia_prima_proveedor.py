from db.db import db
from sqlalchemy.orm import relationship

class MateriaPrimaProveedor(db.Model):
    __tablename__ = 'materia_prima_proveedor'
    id  = db.Column(db.Integer, primary_key=True)
    materiaprima_id = db.Column(db.Integer, db.ForeignKey('materiaprima.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)
    precio = db.Column(db.Float,  nullable=False)
    cantidad = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    proveedor = relationship("Proveedor", backref="materia_prima_proveedor")
    materiaprima = relationship("MateriaPrima", backref="materia_prima_proveedor")

    def serialize(self):
        return {
            "id": self.id,
            "materiaprima": self.materiaprima.serialize(),
            "proveedor": self.proveedor.nombre,
            "precio": float("%.2f" % self.precio),
            "cantidad": self.cantidad,
            "tipo": self.tipo,
            "created_at": str(self.created_at)
        }