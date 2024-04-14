from db.db import db

class CorteDiario(db.Model):
    __tablename__ = "corteDiario"
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    total = db.Column(db.Numeric(10, 2), nullable=False)
    totalEntrada = db.Column(db.Numeric(10, 2), nullable=False)
    totalSalida = db.Column(db.Numeric(10, 2), nullable=False)
    totalEfectivo = db.Column(db.Numeric(10, 2), nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'fecha': self.fecha,
            'total': str(self.total),
            'totalEntrada' : str(self.totalEntrada),
            'totalSalida' : str(self.totalSalida),
            'totalEfectivo' : str(self.totalEfectivo)
        }
    
