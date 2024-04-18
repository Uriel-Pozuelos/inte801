from flask_wtf import Form
from wtforms import StringField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Length


class InventarioMPForm(Form):
    cantidad = IntegerField("Cantidad a comprar",
                            validators=[DataRequired(
                                message="La cantidad es requerida")],
                            render_kw={
                                "class": "input input-bordered input-primary w-full max-w-xs text-black"
                            })

    caducidad = DateTimeField("Fecha de caducidad")

    created_at = DateTimeField('Fecha de Creación')
