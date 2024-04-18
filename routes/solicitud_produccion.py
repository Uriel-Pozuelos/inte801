from flask import Blueprint, request, render_template, redirect, flash
from models.Recetas import Galletas
from models.solicitud_produccion import solicitud_produccion
from models.Inventario_galletas import Inventario_galletas
from datetime import datetime
from lib.d import D
from db.db import db
from forms.SolicitudProduccion import SolicitudForm
from lib.security import safe
from lib.jwt import token_required, allowed_roles, createToken, decodeToken

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

def get_total_gallecta():
    galletas = Galletas.query.all()
    # Crear un diccionario que mapea id de galletas a sus nombres
    galletas_dict = {galleta.id: galleta.totalGalletas for galleta in galletas}
    return galletas_dict

def get_inventario_galletas():
    inventario = Inventario_galletas.query.filter(Inventario_galletas.estatus == 1).all()
    galletas_dict = get_Galletas_dict()
    total_dict = get_total_gallecta()
    registros_modificados = []
    for lote in inventario:
        lote_data = lote.serialize()
        lote_data['nombreGalleta'] = galletas_dict.get(lote.idGalleta, 'Nombre no encontrado')
        lote_data['totalGalleta'] = total_dict.get(lote.idGalleta, 'Número de galletas por receta no encontrado') 
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
    solicitudes_modificadas.reverse()
    return solicitudes_modificadas

@solicitud.route('/solicitud', methods=['GET', 'POST'] )
@token_required
@allowed_roles(roles=["admin", "ventas"])
def index():
    if request.method == 'POST':
        if request.form['action'] == 'enviar':
            # Crear una nueva instancia del modelo solicitud_produccion con los datos del formulario
            cantidad = safe(request.form.get('cantidad'))
            idLoteGalleta = request.form.get('idLoteGalletas')
            inventario = Inventario_galletas.query.get(idLoteGalleta)
            galleta = Galletas.query.get(inventario.idGalleta)
            galletas_x_receta = galleta.totalGalletas
            
            if cantidad =="" or idLoteGalleta == "":
                flash("Completa todos los campos")
                return redirect("/solicitud")
            cantidad = int(cantidad)
            cantidad = cantidad * int(galletas_x_receta)
            if cantidad >= 2147483647:
                flash('Por favor, ingresa un número válido.')
                return(redirect('/solicitud'))
                
            nueva_solicitud = solicitud_produccion(
                idLoteGalletas=idLoteGalleta,
                cantidad=cantidad
            )
            db.session.add(nueva_solicitud)
            db.session.commit()

            if inventario:  # Verificar que el registro exista
                inventario.estatus = 0
                inventario.updated_at = datetime.now()
                db.session.commit()
                flash("Solicitud enviada correctamente")
                return redirect('/solicitud')
        elif request.form['action'] == 'cancelar':
            idSolicitud = request.form.get('idSolicitudCancel')
            if idSolicitud == "":
                flash("Seleccione un tipo de galleta")
                return redirect("/solicitud")
            solicitud_filter =  solicitud_produccion.query.get(idSolicitud)
            solicitud_filter.estatus = 'Cancelada'
            solicitud_filter.updated_at = datetime.now()
            db.session.commit()

            inventario = Inventario_galletas.query.get(solicitud_filter.idLoteGalletas)
            inventario.estatus = 1
            inventario.updated_at = datetime.now()
            db.session.commit()
            flash('Solcitud cancelada correctamente')
            return redirect('/solicitud')
    lotes = get_inventario_galletas()
    solicitudes = get_Solicitud_inventario()
    solicitudes_pendientes = []
    for solicitud in solicitudes:
        if solicitud['estatus'] == 'Pendiente':
            solicitudes_pendientes.append(solicitud)
    return render_template('pages/solicitud_produccion/index.html', solicitudes = solicitudes, lotes=lotes, pendientes = solicitudes_pendientes)