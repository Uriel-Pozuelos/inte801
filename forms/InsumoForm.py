from flask_wtf import Form
from wtforms import (
    StringField,
    IntegerField,
    DateTimeField,
    PasswordField,
    SelectField,
    HiddenField,
    BooleanField,
)
from wtforms.validators import DataRequired, Length, Regexp, Optional


class InsumoForm(Form):
    id = HiddenField("Id", render_kw={"class": "hidden"})

    material = StringField(
        "Materia prima",
        validators=[DataRequired(message="Campo requerido"), Length(max=50), Regexp('^[a-zA-Z ]*$', message='Ingrese solo letras y espacios')],
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black"
        },
    )

    tipo = SelectField(
        "Unidad de medida",
        choices=[
            (
                "",
                "Selecciona una opción",
                {"disabled": "disabled"},
            ),
            ("litros", "Litros"),
            ("kilos", "Kilos"),
            ("gramos", "Gramos"),
            ("mililitros", "Mililitros"),
            ("unidad", "Unidad"),
        ],
        render_kw={
            "class": "select select-bordered select-primary w-full max-w-xs text-black"
        },
        default="",
    )

    estatus = BooleanField("Estatus")

    created_at = DateTimeField("created_at")

    updated_at = DateTimeField("updated_at")

    deleted_at = DateTimeField("deleted_at")


class InsumoEditForm(Form):
    id = IntegerField("id")

    material = StringField("material")

    tipo = StringField("tipo")

    estatus = BooleanField("Estatus")

    created_at = DateTimeField("created_at")

    updated_at = DateTimeField("updated_at")

    deleted_at = DateTimeField("deleted_at")
