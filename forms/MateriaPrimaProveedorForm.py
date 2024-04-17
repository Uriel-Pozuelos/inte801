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
        validators=[
            DataRequired("El precio es requerido"),
            Length(max=5),
            Regexp(r"^\d+\.\d{2}$"),
        ],
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black",
            "type": "number",
        },
    )

    cantidad = IntegerField(
        "Cantidad",
        validators=[
            DataRequired("La cantidad es requerida"),
            Length(min=1, max=5),
            Regexp(r"^\d{1,5}$"),
        ],
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black",
            "type": "number",
        },
    )

    tipo = SelectField(
        "Presentación",
        choices=[
            ("", "Selecciona una opción", {"disabled": "disabled"}),
            ("Bolsa_100g 100g", "Bolsa 100g"),
            ("Bolsa_250g 250g", "Bolsa 250g"),
            ("Bolsa_500g 500g", "Bolsa 500g"),
            ("Bolsa_1kg 1kg", "Bolsa 1kg"),
            ("Bolsa_5kg 5kg", "Bolsa 5kg"),
            ("Bolsa_25kg 25kg", "Bolsa 25kg"),
            ("Costal_50 50kg", "Costal grande 50kg"),
            ("Paquete_500g 500g", "Paquete 500g"),
            ("Paquete_1kg 1kg", "Paquete 1kg"),
            ("Paquete_250g 250g", "Paquete 250g"),
            ("Barra_100g 100g", "Barra 100g"),
            ("Barra_250g 250g", "Barra 250g"),
            ("Barra_500g 500g", "Barra 500g"),
            ("Carton_12_huevos 12", "Docena de huevos"),
            ("Carton_18_huevos 18", "Carton 18 huevos"),
            ("Carton_30_huevos 30", "Carton 30 huevos"),
            ("Carton_60_huevos 60", "Carton 60 huevos"),
            ("Frasco_50ml 50ml", "Frasco 50ml"),
            ("Frasco_100ml 100ml", "Frasco 100ml"),
            ("Frasco_250ml 250ml", "Frasco 250ml"),
            ("Frasco_500ml 500ml", "Frasco 500ml"),
            ("Botella_250ml 250ml", "Botella 250ml"),
            ("Botella_500ml 500ml", "Botella 500ml"),
            ("Botella_1lt 1lt", "Botella 1lt"),
            ("Sobre_10g 10g", "Sobre 10g"),
            ("Galón_4lt 4lt", "Galón 4lt"),
            ("Galón_20lt 20lt", "Galón 20lt"),
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

    cantidad_edit = IntegerField(
        "Cantidad por presentación",
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black",
            "type": "number",
        },
    )

    tipo_edit = SelectField(
        "Presentación",
        choices=[
            ("", "Selecciona una opción", {"disabled": "disabled"}),
            ("Bolsa_100g 100g", "Bolsa 100g"),
            ("Bolsa_250g 250g", "Bolsa 250g"),
            ("Bolsa_500g 500g", "Bolsa 500g"),
            ("Bolsa_1kg 1kg", "Bolsa 1kg"),
            ("Bolsa_5kg 5kg", "Bolsa 5kg"),
            ("Bolsa_25kg 25kg", "Bolsa 25kg"),
            ("Costal_50 50kg", "Costal grande 50kg"),
            ("Paquete_500g 500g", "Paquete 500g"),
            ("Paquete_1kg 1kg", "Paquete 1kg"),
            ("Paquete_250g 250g", "Paquete 250g"),
            ("Barra_100g 100g", "Barra 100g"),
            ("Barra_250g 250g", "Barra 250g"),
            ("Barra_500g 500g", "Barra 500g"),
            ("Carton_12_huevos 12", "Docena de huevos"),
            ("Carton_18_huevos 18", "Carton 18 huevos"),
            ("Carton_30_huevos 30", "Carton 30 huevos"),
            ("Carton_60_huevos 60", "Carton 60 huevos"),
            ("Frasco_50ml 50ml", "Frasco 50ml"),
            ("Frasco_100ml 100ml", "Frasco 100ml"),
            ("Frasco_250ml 250ml", "Frasco 250ml"),
            ("Frasco_500ml 500ml", "Frasco 500ml"),
            ("Botella_250ml 250ml", "Botella 250ml"),
            ("Botella_500ml 500ml", "Botella 500ml"),
            ("Botella_1lt 1lt", "Botella 1lt"),
            ("Sobre_10g 10g", "Sobre 10g"),
            ("Galón_4lt 4lt", "Galón 4lt"),
            ("Galón_20lt 20lt", "Galón 20lt"),
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

    proveedor_id_del = StringField(
        "Proveedor",
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black",
            "readonly": "readonly",
        },
    )

    precio_del = FloatField(
        "Precio unitario",
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black",
            "readonly": "readonly",
        },
    )

    cantidad_del = IntegerField(
        "Cantidad por presentación",
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black"
        },
    )

    tipo_del = StringField(
        "Presentación",
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black"
        },
    )

    created_at = DateTimeField("created_at")
