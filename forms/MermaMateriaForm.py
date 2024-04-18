from flask_wtf import Form
from wtforms import (
    StringField,
    IntegerField,
    TextAreaField,
    DateTimeField,
    SelectField)
from wtforms.validators import (
    DataRequired,
    Length,
    NumberRange)


class MermaMateriaForm(Form):
    merma_tipo = StringField(
        "Causa de la merma",
        validators=[
            DataRequired(message="El tipo de merma es requerido")
        ],
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black",
            "readonly": True,
            "value": "Control de calidad"
        })

    merma_fecha = DateTimeField(
        "Fecha de merma",
        validators=[
            DataRequired(message='La fecha de la merma es obligatoria')
        ],
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black",
            "readonly": True
        }
    )

    cantidad = IntegerField(
        "Cantidad de materia prima",
        validators=[
            DataRequired(message=u'La cantidad es obligatoria'),
            NumberRange(min=1, message=u'Debe ser un número mayor a cero')
        ],
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black",
            "placeholder": "Gramos, mililitros o piezas"
        }
    )

    justificacion = TextAreaField(
        "Justificación de la merma",
        validators=[
            DataRequired(message="La justificación es requerida")
        ],
        render_kw={
            "class": "textarea textarea-bordered textarea-primary w-full max-w-xs text-black",
            "rows": 7,
        }
    )
