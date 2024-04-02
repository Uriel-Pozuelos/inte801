from db.db import db

class MateriaPrimaProveedor(db.Model):
    __tablename__ = 'materia_prima_proveedor'
    materia_prima_id = db.Column(db.Integer, db.ForeignKey('MateriaPrima.id'), primary_key=True)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedores.id'), primary_key=True)

class MateriaPrima(db.Model):
    __tablename__ = 'MateriaPrima'
    id = db.Column(db.Integer, primary_key=True)
    material = db.Column(db.String(255), nullable=False)
    cantidad = db.Column(db.DECIMAL(10,2), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    
    # Relación muchos a muchos con Proveedor
    proveedores = db.relationship('Proveedor', secondary='materia_prima_proveedor', backref=db.backref('materia_primas', lazy='dynamic'))

    def serialize(self):
        return {
            'id': self.id,
            'material': self.material,
            'cantidad': str(self.cantidad),  # Convertir a string para la serialización JSON
            'tipo': self.tipo
        }

class Galletas(db.Model):
    __tablename__ = 'Galletas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.DECIMAL(10,2), nullable=False)
    cantidad = db.Column(db.DECIMAL(10,2), nullable=False)
    enable = db.Column(db.Integer, default=1)
    descripcion = db.Column(db.Text)
    receta = db.Column(db.Text)

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'cantidad': self.cantidad,
            'enable': self.enable,
            'descripcion': self.descripcion,
            'receta': self.receta
        }
    

class Ingredientes(db.Model):
    __tablename__ = 'ingredientes'
    id = db.Column(db.Integer, primary_key=True)
    galleta_id = db.Column(db.Integer, db.ForeignKey('Galletas.id'), nullable=False)
    material_id = db.Column(db.Integer, db.ForeignKey('MateriaPrima.id'), nullable=False)
    cantidad = db.Column(db.DECIMAL(10,2), nullable=False)
    

    def serialize(self):
        return {
            'id': self.id,
            'galleta_id': self.galleta_id,
            'material_id': self.material_id,
            'cantidad': self.cantidad
        }

