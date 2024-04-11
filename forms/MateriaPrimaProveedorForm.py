from flask_wtf import Form
from wtforms import StringField, IntegerField, DateTimeField, PasswordField, SelectField, HiddenField, FloatField
from wtforms.validators import DataRequired, Length, Regexp, Optional


class MateriaPrimaProveedorForm(Form):
    id = HiddenField('id', validators=[
        Optional(),
    ], render_kw={"class": "hidden"})

    materiaprima_id = IntegerField('materiaprima_id')

    proveedor_id = IntegerField('proveedor_id')

    precio = FloatField('precio', validators=[
        DataRequired('El precio es requerido')
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

    cantidad = IntegerField("cantidad", validators=[
        DataRequired('La cantidad es requerida')
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

    tipo = SelectField('tipo', choices=[
        ("kilos", "Kilos"),
        ("litros", "Litros"),
        ("gramos", "Gramos"),
        ("mililitros", "Mililitros"),
        ("piezas", "Piezas"),
        ("galones", "Galones"),
        ("caja", "Caja"),
        ("bolsa", "Bolsa"),
        ("paquete", "Paquete"),
        ("sobre", "Sobre"),
        ("huevos", "Huevos")
    ])

    created_at = DateTimeField('created_at')
