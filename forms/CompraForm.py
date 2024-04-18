from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length

class CompraForm(Form):
    id_proveedor = IntegerField('Proveedor', validators=[
        DataRequired(message="El proveedor es obligatorio.")
    ], render_kw={"class": "input input-bordered input-primary w-full max-w-xs text-black"})
    
    id_usuario = IntegerField('Usuario', validators=[
        DataRequired(message="El usuario es obligatorio.")
    ], render_kw={"class": "input input-bordered input-primary w-full max-w-xs text-black"})
    
    created_at = DateTimeField('Fecha de creación')