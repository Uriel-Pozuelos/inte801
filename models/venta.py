from db.db import db

class Venta(db.Model):
    __tablename__ = "venta"
    id = db.Column(db.Integer, primary_key=True)
    fecha_venta = db.Column(db.DateTime, nullable=False)
    total = db.Column(db.Numeric(10, 2), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    idUsuario = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    detalles_venta = db.relationship("DetalleVenta", backref="venta", lazy=True)
    
    def serialize(self):
        return {
            'id': self.id,
            'fecha_venta': self.fecha_venta,
            'total': str(self.total),
            'created_at': self.created_at,
            'idUsuario': self.idUsuario
        }