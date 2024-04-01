from db.db import db

class Proveedor(db.Model):
    __tablename__ = "proveedores"
    id = db.Column(db.Integer, primary_key=True)
    nombre_empresa = db.Column(db.String(255), nullable=False)
    direccion_empresa = db.Column(db.String(255), nullable=False)
    telefono_empresa = db.Column(db.String(13), nullable=False)
    nombre_atencion = db.Column(db.String(255), nullable=False)
    productos = db.Column(db.String(255), nullable=False)
    estatus = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    deleted_at = db.Column(db.DateTime)

    def serialize(self):
        return {
            'id': self.id,
            'nombre_empresa': self.nombre_empresa,
            'direccion_empresa': self.direccion_empresa,
            'telefono_empresa': self.telefono_empresa,
            'nombre_atencion': self.nombre_atencion,
            'productos': self.productos,
            'estatus': self.estatus,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'deleted_at': self.deleted_at
        }