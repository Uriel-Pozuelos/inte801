from flask_wtf import Form
from wtforms import StringField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Length

class InventarioMPForm(Form):
    id_materia_prima = IntegerField('ID Materia Prima')
    
    cantidad = StringField('Cantidad', validators=[
        DataRequired(message="La cantidad es obligatoria.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    nombre_proveedor = StringField('Nombre del Proveedor', validators=[
        DataRequired(message="El nombre del proveedor es obligatorio.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    caducidad = DateTimeField('Caducidad', validators=[
        DataRequired(message="La caducidad es obligatoria.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    mermas_caducidad = IntegerField('Mermas por Caducidad', validators=[
        DataRequired(message="Las mermas por caducidad son obligatorias.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    mermas_produccion = IntegerField('Mermas por Producción', validators=[
        DataRequired(message="Las mermas por producción son obligatorias.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    created_at = DateTimeField('Fecha de Creación')