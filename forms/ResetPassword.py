from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import Length, DataRequired, EqualTo, Regexp


class ResetPasswordForm(Form):
    correo = StringField('Correo', validators=[
        DataRequired(message="El correo es obligatorio."),
        Length(min=4, max=25, message="El correo debe tener entre 4 y 25 caracteres.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

    password = PasswordField('Contraseña', validators=[
        DataRequired(message="La contraseña es obligatoria."),
        Length(min=8, max=25, message="La contraseña debe tener entre 8 y 25 caracteres."),
        Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+{}|:<>?]).+$',
               message="La contraseña debe contener al menos una mayúscula, una minúscula, un número y un caracter especial.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

    confirm_password = PasswordField('Confirmar contraseña', validators=[
        DataRequired(message="La confirmación de la contraseña es obligatoria."),
        Length(min=8, max=25, message="La confirmación de la contraseña debe tener entre 8 y 25 caracteres."),
        EqualTo('password', message='Las contraseñas deben coincidir.')
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
