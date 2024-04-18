from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, DateTimeField, SelectField
from wtforms.validators import DataRequired, Length


class CompraForm(Form):
    id_proveedor = SelectField(
        "Proveedor",
        choices=[
            ("", "Seleccione un proveedor"),
        ],
        validators=[DataRequired("El proveedor es requerido")],
        render_kw={
            "class": "select select-bordered select-primary w-full max-w-xs text-black"
        },
    )

    id_usuario = IntegerField("Usuario")

    created_at = DateTimeField("Fecha de creación")
