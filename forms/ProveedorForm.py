from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Length

class ProveedorForm():
    nombre_empresa = StringField('Nombre de la empresa', validators=[
        DataRequired(message="El nombre de la empresa es obligatorio."),
        Length(min=4, max=25, message="El nombre de la empresa debe tener entre 4 y 25 caracteres.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    direccion_empresa = StringField('Dirección de la empresa', validators=[
        DataRequired(message="La dirección de la empresa es obligatoria."),
        Length(min=4, max=25, message="La dirección de la empresa debe tener entre 4 y 25 caracteres.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    telefono_empresa = StringField('Teléfono de la empresa', validators=[
        DataRequired(message="El teléfono de la empresa es obligatorio."),
        Length(min=13, max=13, message="El teléfono de la empresa debe tener 13 caracteres.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    nombre_encargado = StringField('Nombre de la persona de atención', validators=[
        DataRequired(message="El nombre de la persona de atención es obligatorio."),
        Length(min=4, max=25, message="El nombre de la persona de atención debe tener entre 4 y 25 caracteres.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    created_at = DateTimeField('Fecha de creación')
    updated_at = DateTimeField('Fecha de actualización')
    deleted_at = DateTimeField('Fecha de eliminación')
    
class ProveedorEditForm():
    id = IntegerField("id")

    nombre_empresa  = StringField('Nombre de la empresa')

    direccion_empresa = StringField('Dirección de la empresa')

    telefono_empresa = StringField('Teléfono de la empresa')

    nombre_encargado = StringField('Nombre del encargado')

    updated_at = DateTimeField('Fecha de actualización')