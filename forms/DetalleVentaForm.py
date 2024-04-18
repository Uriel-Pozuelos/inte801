from flask_wtf import Form
from wtforms import StringField, IntegerField, DateTimeField, SelectField, RadioField, FloatField
from wtforms.validators import DataRequired, Length


class DetalleVentaForm(Form):
    venta_id = IntegerField('', validators=[
        DataRequired(message="El ID de venta es obligatorio.")])
    
    galleta_id = IntegerField('', validators=[
        DataRequired(message="El ID de galleta es obligatorio.")])
    
    cantidad = IntegerField('Cantidad', validators=[
        DataRequired(message="La cantidad es obligatoria."),
        Length(min=1, max=10000, message="La cantidad debe ser mayor a 0 y menor a 10000" )],
        default=1, 
        render_kw={"class": "border border-0 rounded-md w-full max-w-md text-gray-600 p-2"})
    
    precio_unitario = FloatField('Precio Unitario', validators=[
        DataRequired(message="El precio unitario es obligatorio.")
    ], render_kw={"class": "border border-0 rounded-md w-full max-w-md text-black p-2"})
    
    created_at = DateTimeField('', validators=[
        DataRequired(message="La fecha de creación es obligatoria.")])

    galleta = SelectField('Galletas', coerce=int)
    
    tipoVenta = RadioField('Tipo venta', choices=[('1','Paquete 1kg'), ('2','Paquete 700g'), ('3','Unidad')], default='3', 
                        )