from flask_wtf import Form
from wtforms import StringField, IntegerField, DateTimeField, SelectField, RadioField
from wtforms.validators import DataRequired

class VentaForm(Form):
    venta_id = IntegerField('')

    fecha_venta = DateTimeField('', validators=[
        DataRequired(message="La fecha de venta es obligatoria.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    total = IntegerField('Total', validators=[
        DataRequired(message="El total es obligatorio.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    idUsuario = IntegerField('')
    
    created_at = DateTimeField('', validators=[
        DataRequired(message="La fecha de creación es obligatoria.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
