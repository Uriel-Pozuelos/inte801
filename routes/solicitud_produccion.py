from flask import Blueprint, request, render_template
from models.Recetas import Galletas
from models.solicitud_produccion import solicitud_produccion
from models.Inventario_galletas import Inventario_galletas
from datetime import datetime
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

def get_inventario_galletas():
    inventario = Inventario_galletas.query.filter(Inventario_galletas.estatus == 1).all()
    galletas_dict = get_Galletas_dict()
    registros_modificados = []
    for lote in inventario:
        lote_data = lote.serialize()
        lote_data['nombreGalleta'] = galletas_dict.get(lote.idGalleta, 'Nombre no encontrado')
        registros_modificados.append(lote_data)
    
    return registros_modificados

def get_Galleta_nombre_por_idLote(idLoteGalletas):
    inventario_item = Inventario_galletas.query.filter_by(idLoteGalletas=idLoteGalletas).first()
    if inventario_item:
        galletas_dict = get_Galletas_dict()
        return galletas_dict.get(inventario_item.idGalleta, 'Nombre no encontrado')
    return 'Lote no encontrado'

def get_Solicitud_inventario():
    solicitudes = solicitud_produccion.query.all()
    # No necesitas obtener el diccionario de galletas aquí si ajustas la lógica según lo sugerido
    solicitudes_modificadas = []
    for solicitud in solicitudes:
        solicitud_data = solicitud.serialize()
        solicitud_data['nombreGalleta'] = get_Galleta_nombre_por_idLote(solicitud.idLoteGalletas)
        solicitudes_modificadas.append(solicitud_data)
    return solicitudes_modificadas

@solicitud.route('/solicitud', methods=['GET', 'POST'] )
def index():
    form = SolicitudForm(request.form)
    if request.method == 'POST':
        # Crear una nueva instancia del modelo solicitud_produccion con los datos del formulario
        nueva_solicitud = solicitud_produccion(
            idLoteGalletas=form.idLoteGalletas.data,
            cantidad=form.cantidad.data
        )
        db.session.add(nueva_solicitud)
        db.session.commit()

        inventario = Inventario_galletas.query.get(form.idLoteGalletas.data)
        if inventario:  # Verificar que el registro exista
            inventario.estatus = 0
            inventario.updated_at = datetime.now()
            db.session.commit()

    lotes = get_inventario_galletas()
    print(f"Lotes: {lotes}")
    solicitudes = get_Solicitud_inventario()
    return render_template('pages/solicitud_produccion/index.html', form=form, solicitudes = solicitudes, lotes=lotes)