from db.db import db

class DetalleVenta(db.Model):
    __tablename__ = "detalle_venta"
    id = db.Column(db.Integer, primary_key=True)
    venta_id = db.Column(db.Integer, db.ForeignKey("venta.id"), nullable=False)
    galleta_id = db.Column(db.Integer, db.ForeignKey("galletas.id"), nullable=False)
    producto = db.Column(db.String(255), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    galleta = db.relationship("Galletas", backref="detalle_venta", lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'venta_id': self.venta_id,
            'producto': self.producto,
            'cantidad': self.cantidad,
            'precio_unitario': self.precio_unitario,
            'created_at': self.created_at
        }