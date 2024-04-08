from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length

class MermaMateriaForm(Form):    
    idInventarioMaterias = IntegerField('Inventario de Materias', validators=[
        DataRequired(message="El inventario de materias es obligatorio.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    merma_tipo = StringField('Tipo de Merma', validators=[
        DataRequired(message="El tipo de merma es obligatorio.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    merma_fecha = StringField('Fecha de Merma', validators=[
        DataRequired(message="La fecha de merma es obligatoria.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    cantidad = IntegerField('Cantidad', validators=[
        DataRequired(message="La cantidad es obligatoria.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    created_at = DateTimeField('Fecha de creación')
    
    id_produccion = IntegerField('Producción')
    
    justificacion = TextAreaField('Justificación', validators=[
        DataRequired(message="La justificación es obligatoria.")
    ], render_kw={"class": "textarea textarea-bordered w-full text-black"})
    
    id_proveedor = IntegerField('Proveedor')