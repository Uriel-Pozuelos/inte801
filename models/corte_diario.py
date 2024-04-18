from db.db import db

class CorteDiario(db.Model):
    __tablename__ = "cortediario"
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    totalEntrada = db.Column(db.Numeric(10, 2), nullable=False)
    totalSalida = db.Column(db.Numeric(10, 2), nullable=False)
    totalEfectivo = db.Column(db.Numeric(10, 2), nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'fecha': self.fecha,
            'totalEntrada' : str(self.totalEntrada),
            'totalSalida' : str(self.totalSalida),
            'totalEfectivo' : str(self.totalEfectivo)
        }
    
