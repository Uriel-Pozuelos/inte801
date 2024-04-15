from flask_wtf import Form
from wtforms import (
    StringField,
    IntegerField,
    DateTimeField,
    PasswordField,
    SelectField,
    HiddenField,
    FloatField,
)
from wtforms.validators import DataRequired, Length, Regexp, Optional


class MateriaPrimaProveedorForm(Form):
    id = HiddenField(
        "id",
        validators=[
            Optional(),
        ],
        render_kw={"class": "hidden"},
    )

    materiaprima_id = IntegerField("materiaprima_id")

    proveedor_id = SelectField(
        "Proveedor",
        choices=[],
        validators=[DataRequired("El proveedor es requerido")],
        render_kw={
            "class": "select select-bordered select-primary w-full max-w-xs text-black"
        },
    )

    precio = FloatField(
        "Precio unitario",
        validators=[DataRequired("El precio es requerido"), Length(
            max=5), Regexp(r"^\d+\.\d{2}$")],
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black",
            "type": "number",
        },
    )

    cantidad = IntegerField(
        "Cantidad",
        validators=[DataRequired("La cantidad es requerida"), Length(
            min=1, max=5), Regexp(r"^\d{1,5}$")],
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black",
            "type": "number",
        },
    )

    tipo = SelectField(
        "Presentación",
        choices=[
            ("", "Selecciona una opción", {"disabled": "disabled"}),
            ("Bolsa 100g", "Bolsa 100g"),
            ("Bolsa 250g", "Bolsa 250g"),
            ("Bolsa 500g", "Bolsa 500g"),
            ("Bolsas 1kg", "Bolsas 1kg"),
            ("Bolsas 5kg", "Bolsas 5kg"),
            ("Bolsas 25kg", "Bolsas 25kg"),
            ("Costal grande 50kg", "Costal grande 50kg"),
            ("Paquete 500g", "Paquete 500g"),
            ("Paquete 1kg", "Paquete 1kg"),
            ("Paquete 250g", "Paquete 250g"),
            ("Barra 100g", "Barra 100g"),
            ("Barra 250g", "Barra 250g"),
            ("Barra 500g", "Barra 500g"),
            ("Docena", "Docena"),
            ("Carton 18 huevos", "Carton 18 huevos"),
            ("Carton 30 huevos", "Carton 30 huevos"),
            ("Carton 60 huevos", "Carton 60 huevos"),
            ("Frasco 50ml", "Frasco 50ml"),
            ("Frascos 100ml", "Frascos 100ml"),
            ("Frasco 250ml", "Frasco 250ml"),
            ("Frasco 500ml", "Frasco 500ml"),
            ("Botella 250ml", "Botella 250ml"),
            ("Botella 500ml", "Botella 500ml"),
            ("Botella 1lt", "Botella 1lt"),
            ("Sobre 10g", "Sobre 10g"),
        ],
        validators=[DataRequired("La presentación es requerida")],
        render_kw={
            "class": "select select-bordered select-primary w-full max-w-xs text-black"
        },
        default="",
    )

    created_at = DateTimeField("created_at")


class MateriaPrimaProveedorEditForm(Form):
    id = IntegerField("id")

    materiaprima_id_edit = IntegerField("materiaprima_id")

    proveedor_id_edit = SelectField(
        "Proveedor",
        choices=[],
        render_kw={
            "class": "select select-bordered select-primary w-full max-w-xs text-black"
        },
    )

    precio_edit = FloatField(
        "Precio unitario",
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black",
            "type": "number",
        },
    )

    cantidad_edit = IntegerField("Cantidad por presentación", render_kw={
        "class": "input input-bordered input-primary w-full max-w-xs text-black",
        "type": "number",
    })

    tipo_edit = SelectField(
        "Presentación",
        choices=[
            ("", "Selecciona una opción", {"disabled": "disabled"}),
            ("Bolsa 100g", "Bolsa 100g"),
            ("Bolsa 250g", "Bolsa 250g"),
            ("Bolsa 500g", "Bolsa 500g"),
            ("Bolsas 1kg", "Bolsas 1kg"),
            ("Bolsas 5kg", "Bolsas 5kg"),
            ("Bolsas 25kg", "Bolsas 25kg"),
            ("Costal grande 50kg", "Costal grande 50kg"),
            ("Paquete 500g", "Paquete 500g"),
            ("Paquete 1kg", "Paquete 1kg"),
            ("Paquete 250g", "Paquete 250g"),
            ("Barra 100g", "Barra 100g"),
            ("Barra 250g", "Barra 250g"),
            ("Barra 500g", "Barra 500g"),
            ("Docena", "Docena"),
            ("Carton 18 huevos", "Carton 18 huevos"),
            ("Carton 30 huevos", "Carton 30 huevos"),
            ("Carton 60 huevos", "Carton 60 huevos"),
            ("Frasco 50ml", "Frasco 50ml"),
            ("Frascos 100ml", "Frascos 100ml"),
            ("Frasco 250ml", "Frasco 250ml"),
            ("Frasco 500ml", "Frasco 500ml"),
            ("Botella 250ml", "Botella 250ml"),
            ("Botella 500ml", "Botella 500ml"),
            ("Botella 1lt", "Botella 1lt"),
            ("Sobre 10g", "Sobre 10g"),
        ],
        validators=[DataRequired("La presentación es requerida")],
        render_kw={
            "class": "select select-bordered select-primary w-full max-w-xs text-black"
        },
        default="",
    )

    created_at = DateTimeField("created_at")


class MateriaPrimaProveedorDelForm(Form):
    id = IntegerField("id")

    materiaprima_id_del = IntegerField("materiaprima_id")

    proveedor_id_del = StringField("Proveedor",
                                   render_kw={
                                       "class": "input input-bordered input-primary w-full max-w-xs text-black", "readonly": "readonly"})

    precio_del = FloatField("Precio unitario", render_kw={
        "class": "input input-bordered input-primary w-full max-w-xs text-black", "readonly": "readonly"})

    cantidad_del = IntegerField("Cantidad por presentación", render_kw={
        "class": "input input-bordered input-primary w-full max-w-xs text-black"
    })

    tipo_del = StringField("Presentación", render_kw={
        "class": "input input-bordered input-primary w-full max-w-xs text-black"
    })

    created_at = DateTimeField("created_at")
