from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import Length, DataRequired, EqualTo, Regexp, ValidationError


def validar_contra_archivo(form, field):
  password = field.data
  if password is None:
    raise ValidationError("La contraseña es obligatoria.")
  with open("password.txt", "r") as f:
    if password + "\n" in f.readlines():
      raise ValidationError("Esta contraseña no es segura, por favor elige otra.")
    
class ResetPasswordForm(Form):

    password = PasswordField('Contraseña', validators=[
        DataRequired(message="La contraseña es obligatoria."),
        validar_contra_archivo,
        Length(min=8, max=25, message="La contraseña debe tener entre 8 y 25 caracteres."),
        Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+{}|:<>?]).+$',
               message="La contraseña debe contener al menos una mayúscula, una minúscula, un número y un caracter especial.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

    confirm_password = PasswordField('Confirmar contraseña', validators=[
        validar_contra_archivo,
        DataRequired(message="La confirmación de la contraseña es obligatoria."),
        Length(min=8, max=25, message="La confirmación de la contraseña debe tener entre 8 y 25 caracteres."),
        EqualTo('password', message='Las contraseñas deben coincidir.')
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
