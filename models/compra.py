from db.db import db

class Compra(db.Model):
    __tablename__ = "compras"
    id = db.Column(db.Integer, primary_key=True)
    id_proveedor = db.Column(db.Integer, db.ForeignKey("proveedores.id"), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    detalle_compra = db.relationship("DetalleCompra", backref="compra", lazy=True)
    
    def serialize(self):
        return {
            'id': self.id,
            'id_proveedor': self.id_proveedor,
            'id_usuario': self.id_usuario,
            'created_at': self.created_at
        }