from flask_wtf import Form
from wtforms import SelectField, IntegerField
from wtforms.validators import InputRequired, NumberRange

class ProduccionForm(Form):
    idGalleta = SelectField('Nombre de Galleta', coerce=int, validators=[
        InputRequired(message="Selecciona una galleta.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

    cantidad = IntegerField('Cantidad de Galletas', validators=[
        InputRequired(message="La cantidad es obligatoria."),
        NumberRange(min=1, message="La cantidad debe ser al menos 1.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black bg-white"})