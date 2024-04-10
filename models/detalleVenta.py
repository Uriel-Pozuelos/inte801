from db.db import db

class DetalleVenta(db.Model):
    __tablename__ = "detalleventa"
    id = db.Column(db.Integer, primary_key=True)
    venta_id = db.Column(db.Integer, db.ForeignKey("venta.id"))
    galleta_id = db.Column(db.Integer, db.ForeignKey("galletas.id"))
    cantidad = db.Column(db.Numeric(10, 2), nullable=False)
    precio_unitario = db.Column(db.Numeric(10, 2), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    tipoVenta = db.Column(db.String(255), nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'venta_id': self.venta_id,
            'galleta_id': self.galleta_id,
            'cantidad': str(self.cantidad),  
            'precio_unitario': str(self.precio_unitario),
            'created_at': self.created_at,
            'tipoVenta': self.tipoVenta
        }