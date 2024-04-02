from flask_wtf import Form
from wtforms import StringField, IntegerField, DateTimeField, PasswordField,SelectField
from wtforms.validators import DataRequired, Length


class UsuarioForm(Form):
  nombre = StringField('Nombre', validators=[
    DataRequired(message="El nombre es obligatorio.")
  ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

  apellido = StringField('Apellido', validators=[
    DataRequired(message="El apellido es obligatorio.")
  ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

  email = StringField('Email', validators=[
    DataRequired(message="El email es obligatorio.")
  ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

  password = PasswordField('Password', validators=[
    DataRequired(message="El password es obligatorio.")
  ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

  rol = SelectField('Rol', choices=[('compras', 'Compras'), ('ventas', 'Ventas'), ('produccion', 'Producción'), ('admin', 'Administrador')], validators=[
    DataRequired(message="El rol es obligatorio.")
  ], render_kw={"class": "select select-bordered w-full max-w-xs"})

