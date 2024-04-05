from db.db import db

class MateriaPrimaProveedor(db.Model):
    __tablename__ = 'materia_prima_proveedor'
    materiaprima_id = db.Column(db.Integer, db.ForeignKey('materiaprima.id'), primary_key=True)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), primary_key=True)

    # Relación muchos a muchos con MateriaPrima
    materiaprima = db.relationship('MateriaPrima', backref=db.backref('materia_prima_proveedor', lazy='dynamic'))
    # Relación muchos a muchos con Proveedor
    proveedor = db.relationship('Proveedor', backref=db.backref('materia_prima_proveedor', lazy='dynamic'))

class MateriaPrima(db.Model):
    __tablename__ = 'materiaprima'
    id = db.Column(db.Integer, primary_key=True)
    material = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    estatus = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now(),default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(),default=db.func.now(), onupdate=db.func.now())
    deleted_at = db.Column(db.DateTime, nullable=True)
    

    def serialize(self):
        return {
            'id': self.id,
            'material': self.material,
            'tipo': self.tipo
        }

class Galletas(db.Model):
    __tablename__ = 'galletas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.DECIMAL(10,2), nullable=False)
    enable = db.Column(db.Integer, default=1)
    descripcion = db.Column(db.Text)
    receta = db.Column(db.Text)
    totalGalletas = db.Column(db.Integer, default=0,nullable=False)
    pesoGalleta = db.Column(db.DECIMAL(10,2), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now(),default=db.func.now())

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'enable': self.enable,
            'descripcion': self.descripcion,
            'receta': self.receta,
            'totalGalletas': self.totalGalletas,
            'pesoGalleta': self.pesoGalleta,
            'created_at': self.created_at
        }
    

class Ingredientes(db.Model):
    __tablename__ = 'ingredientes'
    id = db.Column(db.Integer, primary_key=True)
    galleta_id = db.Column(db.Integer, db.ForeignKey('galletas.id'), nullable=False)
    material_id = db.Column(db.Integer, db.ForeignKey('materiaprima.id'), nullable=False)
    cantidad = db.Column(db.DECIMAL(10,2), nullable=False)
    estatus = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now(),default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(),default=db.func.now(), onupdate=db.func.now())
    deleted_at = db.Column(db.DateTime, nullable=True)
    
    # Relación muchos a uno con Galletas
    galletas = db.relationship('Galletas', backref=db.backref('ingredientes', lazy='dynamic'))

    def serialize(self):
        return {
            'id': self.id,
            'galleta_id': self.galleta_id,
            'material_id': self.material_id,
            'cantidad': self.cantidad,
            'estatus': self.estatus,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'deleted_at': self.deleted_at
        }

