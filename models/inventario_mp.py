from db.db import db

class InventarioMP(db.Model):
    __tablename__ = "inventario_mp"
    id_materia_prima = db.Column(db.Integer, db.ForeignKey("materiaprima.id"), nullable=False)
    cantidad = db.Column(db.String(255), nullable=False)
    nombre_proveedor = db.Column(db.String(255), nullable=False)
    caducidad = db.Column(db.DateTime, nullable=False)
    mermas_caducidad = db.Column(db.Integer, nullable=False)
    mermas_produccion = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    
    def serialize(self):
        return {
            'id_materia_prima': self.id_materia_prima,
            'cantidad': self.cantidad,
            'nombre_proveedor': self.nombre_proveedor,
            'caducidad': self.caducidad,
            'mermas_caducidad': self.mermas_caducidad,
            'mermas_produccion': self.mermas_produccion,
            'created_at': self.created_at
        }