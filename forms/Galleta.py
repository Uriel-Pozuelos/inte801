from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField,FloatField,SelectField
from wtforms.validators import DataRequired, Length


class GalletaForm(Form):
  nombre = StringField('Nombre', validators=[
    DataRequired(message="El nombre es obligatorio.")
  ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

  
  pesoGalleta = FloatField('Peso en gramos', validators=[
    DataRequired(message="El peso es obligatorio.")
  ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

 

  descripcion = StringField('Descripción', validators=[
    DataRequired(message="La descripción es obligatoria.")
  ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

  

class Galleta2(Form):
  
  totalGalletas = SelectField('Total de galletas', 
                            choices=[(str(i), str(i)) for i in range(1, 101)], 
                            render_kw={"class": "select select-bordered w-full max-w-xs text-black"})
