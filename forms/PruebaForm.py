from wtforms import StringField
from flask_wtf import Form
from wtforms.validators import Length

class PruebaForm(Form):
  nombre = StringField('nombre',validators=[Length(min=4,max=25)])
