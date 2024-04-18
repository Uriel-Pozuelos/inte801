from flask_wtf import Form
from wtforms import StringField, IntegerField, DateTimeField, SelectField, FloatField
from wtforms.validators import DataRequired, Length


class DetalleCompraForm(Form):
    materia_prima = SelectField(
        "Materia prima",
        choices=[
            ("", "Seleccione una materia prima"),
        ],
        validators=[DataRequired("La materia prima es requerida")],
        render_kw={
            "class": "select select-bordered select-primary w-full max-w-xs text-black"
        },
    )

    precio_materia = FloatField(
        "Precio unitario",
        validators=[
            DataRequired(message="El precio de la materia prima es obligatorio."),
            Length(
                min=1,
                max=100,
                message="El precio de la materia prima debe tener entre 1 y 100 caracteres.",
            ),
        ],
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black"
        },
    )

    cantidad = IntegerField(
        "Cantidad",
        validators=[
            DataRequired(message="La cantidad es obligatoria."),
            Length(
                min=1,
                max=100,
                message="La cantidad debe tener entre 1 y 100 caracteres.",
            ),
        ],
        render_kw={"class": "input input-bordered input-primary w-full max-w-xs text-black"},
    )

    tipo = StringField(
        "Tipo",
        validators=[DataRequired(message="El tipo es obligatorio.")],
        render_kw={"class": "input input-bordered w-full max-w-xs text-black"},
    )

    caducidad = DateTimeField(
        "Caducidad",
        validators=[DataRequired(message="La caducidad es obligatoria.")],
        render_kw={"class": "input input-bordered w-full max-w-xs text-black"},
    )

    created_at = DateTimeField("Fecha de Creación")

    id_compra = IntegerField()
