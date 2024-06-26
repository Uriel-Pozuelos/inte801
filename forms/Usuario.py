from flask_wtf import Form
from wtforms import StringField, IntegerField, DateTimeField, PasswordField,SelectField,HiddenField
from wtforms.validators import DataRequired, Length,Regexp,Optional,ValidationError
import os

def validar_contra_archivo(form, field):
  password = field.data
  if password is None:
    raise ValidationError("La contraseña es obligatoria.")
  with open("password.txt", "r") as f:
    if password + "\n" in f.readlines():
      raise ValidationError("Esta contraseña no es segura, por favor elige otra.")


class UsuarioForm(Form):
  id = HiddenField('id', validators=[
    Optional(),
  ], render_kw={"class": "hidden"})

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
    validar_contra_archivo,
    Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+{}|:<>?]).+$',
                message="La contraseña debe contener al menos una mayúscula, una minúscula, un número y un caracter especial.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

  rol = SelectField('Rol', choices=[('compras', 'Compras'), ('ventas', 'Ventas'), ('produccion', 'Producción'), ('admin', 'Administrador')], validators=[
    DataRequired(message="El rol es obligatorio.")
  ], render_kw={"class": "select select-bordered w-full max-w-xs"})

