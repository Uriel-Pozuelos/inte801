from flask_wtf import Form
from wtforms import StringField, IntegerField, DateTimeField, SelectField, RadioField
from wtforms.validators import DataRequired

class Venta(Form):
    galleta = SelectField('Galleta', choises=[(1, 'Galleta'), (2, 'Galleta2'), (3, 'Galleta3')], 
                        validators=[DataRequired(message="La galleta es obligatoria.")], 
                        render_kw={"class": "input input-bordered w-full max-w-xs text-black"}) 
    cantidad = IntegerField('Cantidad', validators=[DataRequired(message="La cantidad es obligatoria.")],
                            render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    tipo = RadioField('Tipo', choices=[('Caja', 'Caja'), ('Paquete', 'Paquete'), ('Unidad','Unidad'), ('Gramaje', 'Gramaje'), ('Dinero', 'Dinero')],
                        validators=[DataRequired(message="El tipo de venta es obligatorio.")],
                        render_kw={"class": "input input-bordered w-full max-w-xs text-black"})
    
    created_at = DateTimeField('Fecha de creación')
    
