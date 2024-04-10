from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField,FloatField
from wtforms.validators import DataRequired, Length


class GalletaForm(Form):
  nombre = StringField('Nombre', validators=[
    DataRequired(message="El nombre es obligatorio.")
  ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

  precio = FloatField('Precio', validators=[
    DataRequired(message="El precio es obligatorio.")
  ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

  pesoGalleta = FloatField('Peso', validators=[
    DataRequired(message="El peso es obligatorio.")
  ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

  totalGalletas = IntegerField('Total de Galletas', validators=[
    DataRequired(message="El total de galletas es obligatorio.")
  ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

  descripcion = StringField('Descripción', validators=[
    DataRequired(message="La descripción es obligatoria.")
  ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

  receta = TextAreaField('Receta', validators=[
    DataRequired(message="La receta es obligatoria.")
  ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})