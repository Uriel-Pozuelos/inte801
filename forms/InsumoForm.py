from flask_wtf import Form
from wtforms import StringField, IntegerField, DateTimeField, PasswordField, SelectField, HiddenField, BooleanField
from wtforms.validators import DataRequired, Length, Regexp, Optional


class InsumoForm(Form):
    id = HiddenField('Id',render_kw={"class": "hidden"})

    material = StringField('Material', validators=[
        DataRequired(message='Campo requerido')
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

    tipo = StringField('Tipo', validators=[
        DataRequired(message='Campo requerido')
    ], render_kw={"class": "input input-bordered w-full max-w-xs text-black"})

    estatus = BooleanField('Estatus')

    created_at = DateTimeField('created_at')

    updated_at  = DateTimeField('updated_at')

    deleted_at  = DateTimeField('deleted_at')