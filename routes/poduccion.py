from flask import Blueprint, request, render_template, redirect, url_for
from models.Produccion import Produccion
from models.Recetas import Galletas
from models.solicitud_produccion import solicitud_produccion
from lib.d import D
from db.db import db
from forms.Produccion import ProduccionForm
from datetime import datetime

produccion = Blueprint('produccion', __name__, template_folder='templates')
log = D(debug=True)

def get_Galletas():
    galletas = Galletas.query.all()
    return [galleta.serialize() for galleta in galletas]

def get_Galletas_dict():
    galletas = Galletas.query.all()
    # Crear un diccionario que mapea id de galletas a sus nombres
    galletas_dict = {galleta.id: galleta.nombre for galleta in galletas}
    return galletas_dict

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

def get_Solicitud():
    solicitudes = solicitud_produccion.query.filter_by(estatus='pendiente').all()
    return [solicitud.serialize() for solicitud in solicitudes]



def get_Produccion():
    en_produccion = Produccion.query.filter(Produccion.estatus != 'Terminado').all()
    return [produccion.serialize() for produccion in en_produccion]

def get_MateriaPrima():
    en_produccion = Produccion.query.filter(Produccion.estatus != 'Terminado').all()
    return [produccion.serialize() for produccion in en_produccion]


@produccion.route('/produccion', methods=['GET', 'POST'] )
def index():
    form = ProduccionForm(request.form)
    solicitud = get_Solicitud_galleta()
    produccion = get_Produccion()
    
    return render_template('pages/produccion/index.html', solicitud=solicitud, form=form, produccion = produccion)
        
@produccion.route('/revisar_solicitudes', methods=['GET', 'POST'])
def revisar_solicitudes():
    solicitud = get_Solicitud()
    galletas = get_Galletas()

    if request.method == 'POST':
        if 'aceptada' in request.form:
            solicitud_id = request.form.get('solicitud_id')
            solicitud = solicitud_produccion.query.get(solicitud_id)
            solicitud.estatus = 'Aceptada'
            solicitud.updated_at = datetime.now()
            db.session.commit()
            produccion = Produccion(
                idSolicitud = solicitud_id
            )
            db.session.add(produccion)
            db.session.commit()

            return redirect(url_for('produccion.revisar_solicitudes'))
        elif 'rechazada' in request.form:
            justificacion_text = request.form['justificacion']  # Extraer el texto de justificación del formulario
            solicitud_id = request.form.get('solicitud_id')
            solicitud = solicitud_produccion.query.get(solicitud_id)
            if solicitud:  # Verificar que el registro exista
                solicitud.justificacion = justificacion_text  # Actualizar la justificación
                solicitud.estatus = 'Rechazada'  # Cambiar el estatus a 'Rechazado'
                solicitud.updated_at = datetime.now()
                db.session.commit()  # Guardar los cambios en la base de datos
                return redirect(url_for('produccion.revisar_solicitudes'))


    return render_template('pages/produccion/show.html', solicitud=solicitud, galletas = galletas)