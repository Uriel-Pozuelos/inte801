from flask_wtf import Form
from wtforms import StringField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Length

class DetalleCompraForm(Form):
    materia_prima = StringField('Materia Prima', validators=[
        DataRequired(message="La materia prima es obligatoria.")
    ], render_kw={"clFass": "input input-bordered w-full max-w-xs text-black"})
    
    precio_materia = IntegerField('Precio de la Materia Prima', validators=[
        DataRequired(message="El precio de la materia prima es obligatorio.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    cantidad = IntegerField('Cantidad', validators=[
        DataRequired(message="La cantidad es obligatoria.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    tipo = StringField('Tipo', validators=[
        DataRequired(message="El tipo es obligatorio.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    caducidad = DateTimeField('Caducidad', validators=[
        DataRequired(message="La caducidad es obligatoria.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    created_at = DateTimeField('Fecha de Creación')
    
    id_compra = IntegerField()