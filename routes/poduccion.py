from flask import Blueprint, request, render_template, redirect, url_for
from models.Produccion import Produccion
from models.Recetas import Galletas, MateriaPrima
from models.solicitud_produccion import solicitud_produccion
from models.Inventario_galletas import Inventario_galletas
from models.inventario_mp import InventarioMP
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

def get_inventario_galletas():
    inventario = Inventario_galletas.query.all()
    galletas_dict = get_Galletas_dict()
    registros_modificados = []
    for lote in inventario:
        lote_data = lote.serialize()
        lote_data['nombreGalleta'] = galletas_dict.get(lote.idGalleta, 'Nombre no encontrado')
        registros_modificados.append(lote_data)
    return registros_modificados

def get_inventario_dict():
    inventario = get_inventario_galletas()
    inventario_dict = {lote['idLoteGalletas']: lote['nombreGalleta'] for lote in inventario}
    return inventario_dict

def get_Solicitud_inventario():
    solicitudes = solicitud_produccion.query.all()
    inventario_dict = get_inventario_dict()  # Obtener el diccionario de galletas
    # Modificar cada solicitud para reemplazar idGalleta con el nombre de la galleta
    solicitudes_modificadas = []
    for solicitud in solicitudes:
        solicitud_data = solicitud.serialize()
        # Usar el diccionario para obtener el nombre de la galleta
        solicitud_data['nombreGalleta'] = inventario_dict.get(solicitud.idLoteGalletas, 'Nombre no encontrado')
        solicitudes_modificadas.append(solicitud_data)
    return solicitudes_modificadas

def get_solicitud_dict():
    solicitudes = get_Solicitud_inventario()
    inventario_dict = {solicitud['idSolicitud']: solicitud['nombreGalleta'] for solicitud in solicitudes}
    return inventario_dict


def get_Solicitud():
    solicitudes = solicitud_produccion.query.all()
    return [solicitud.serialize() for solicitud in solicitudes]



def get_Produccion():
    en_produccion = Produccion.query.all()
    solicitud_dict = get_solicitud_dict()
    produccion_new = []
    for registro in en_produccion:
        produccion_data = registro.serialize()
        # Usar el diccionario para obtener el nombre de la galleta
        produccion_data['nombreGalleta'] = solicitud_dict.get(registro.idSolicitud, 'Nombre no encontrado')
        produccion_new.append(produccion_data)
    return produccion_new


def get_materia_dict():
    ingredientes = MateriaPrima.query.all()
    ingredientes_dict = {ingrediente.id: ingrediente.material for ingrediente in ingredientes}
    return ingredientes_dict

def get_inventario():
    inventario = InventarioMP.query.all()
    print (inventario)
    ingredientes_dict = get_materia_dict()
    inventario_update = []
    for lote in inventario:
        inventario_data = lote.serialize()
        inventario_data['nombreMateria'] = ingredientes_dict.get(lote.idSolicitud, 'Nombre no encontrado')
        inventario_update.append(inventario_data)
    return inventario_update

#def get_MateriaPrima():
#    en_produccion = Produccion.query.filter(Produccion.estatus != 'Terminado').all()
#    return [produccion.serialize() for produccion in en_produccion]


@produccion.route('/produccion', methods=['GET', 'POST'] )
def index():
    form = ProduccionForm(request.form)
    solicitud = get_Solicitud()
    produccion = get_Produccion()
    produccion_filtro = []
    for registro in produccion:
        if registro['estatus'] != 1:
            produccion_filtro.append(registro)
    inventario_materia = get_inventario()
    inventario_update = []
    for lote in inventario_materia:
        if lote['estatus'] == 1:
            inventario_update.append(lote)
    
    return render_template('pages/produccion/index.html', solicitud=solicitud, form=form, produccion = produccion_filtro, inventario = inventario_update)
        
@produccion.route('/revisar_solicitudes', methods=['GET', 'POST'])
def revisar_solicitudes():
    solicitudes = get_Solicitud_inventario()
    solicitues_filtro = []
    for solicitud in solicitudes:
        if solicitud['estatus'] == "Pendiente":
            solicitues_filtro.append(solicitud)
    galletas = get_Galletas()

    if request.method == 'POST':
        if 'aceptada' in request.form:
            solicitud_id = request.form.get('solicitud_id')
            print(solicitud_id)
            solicitud = solicitud_produccion.query.get(solicitud_id)
            solicitud.estatus = 'Aceptada'
            solicitud.updated_at = datetime.now()
            db.session.commit()
            produccion = Produccion(
                idSolicitud = solicitud_id,
                idUsuario = 1
            )
            db.session.add(produccion)
            db.session.commit()

            return redirect(url_for('produccion.revisar_solicitudes'))
        elif 'rechazada' in request.form:
            justificacion_text = request.form['justificacion']  # Extraer el texto de justificación del formulario
            solicitud_id = request.form.get('reject_solicitud_id')
            solicitud = solicitud_produccion.query.get(solicitud_id)
            print(solicitud.idLoteGalletas)
            if solicitud:  # Verificar que el registro exista
                solicitud.justificacion = justificacion_text  # Actualizar la justificación
                solicitud.estatus = 'Rechazada'  # Cambiar el estatus a 'Rechazado'
                solicitud.updated_at = datetime.now()
                db.session.commit()  # Guardar los cambios en la base de datos
            inventario = Inventario_galletas.query.get(solicitud.idLoteGalletas)
            print(inventario)
            if inventario:
                inventario.estatus = 0
                inventario.updated_at = datetime.now()
                db.session.commit()
                return redirect(url_for('produccion.revisar_solicitudes'))

    return render_template('pages/produccion/show.html', solicitud=solicitues_filtro, galletas = galletas)