from flask import Blueprint, request, render_template
from models.Recetas import Galletas
from models.solicitud_produccion import solicitud_produccion

from lib.d import D
from db.db import db
from forms.SolicitudProduccion import SolicitudForm
solicitud = Blueprint('solicitud', __name__, template_folder='templates')
log = D(debug=True)

def get_Galletas():
    galletas = Galletas.query.all()
    return [galleta.serialize() for galleta in galletas]

def get_Galletas_dict():
    galletas = Galletas.query.all()
    # Crear un diccionario que mapea id de galletas a sus nombres
    galletas_dict = {galleta.id: galleta.nombre for galleta in galletas}
    return galletas_dict

#def get_InventarioGalletas():
 #   inventario_galletas = 

def get_Solicitud_galleta():
    solicitudes = solicitud_produccion.query.all()
    galletas_dict = get_Galletas_dict()  # Obtener el diccionario de galletas
    # Modificar cada solicitud para reemplazar idGalleta con el nombre de la galleta
    solicitudes_modificadas = []
    for solicitud in solicitudes:
        solicitud_data = solicitud.serialize()
        # Usar el diccionario para obtener el nombre de la galleta
        solicitud_data['nombreGalleta'] = galletas_dict.get(solicitud.idGalleta, 'Nombre no encontrado')
        del solicitud_data['idGalleta']  # Opcional: remover el idGalleta si ya no se necesita
        solicitudes_modificadas.append(solicitud_data)
    return solicitudes_modificadas

@solicitud.route('/solicitud', methods=['GET', 'POST'] )
def index():
    form = SolicitudForm(request.form)
    if request.method == 'POST':
        # Crear una nueva instancia del modelo solicitud_produccion con los datos del formulario
        nueva_solicitud = solicitud_produccion(
            idGalleta=form.idGalleta.data,
            cantidad=form.cantidad.data
        )
        db.session.add(nueva_solicitud)
        db.session.commit()

    galletas = get_Galletas()
    solicitudes = get_Solicitud_galleta()
    return render_template('pages/solicitud_produccion/index.html', galletas=galletas, form=form, solicitudes = solicitudes)