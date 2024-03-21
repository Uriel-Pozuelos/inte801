from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import Length, DataRequired


class LoginForm(Form):
    correo = StringField('correo', validators=[
        DataRequired(message="El correo es obligatorio."),
        Length(min=4, max=25, message="El correo debe tener entre 4 y 25 caracteres.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

    password = PasswordField('Contraseña', validators=[
        DataRequired(message="La contraseña es obligatoria."),
        Length(min=4, max=25, message="La contraseña debe tener entre 4 y 25 caracteres.")
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
