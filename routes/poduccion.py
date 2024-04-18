from flask import Blueprint, request, render_template, redirect, url_for, flash
from models.Produccion import Produccion
from models.Recetas import Galletas, MateriaPrima, Ingredientes
from models.solicitud_produccion import solicitud_produccion
from models.Inventario_galletas import Inventario_galletas
from models.inventario_mp import InventarioMP
from models.merma_materia import MermaMateria
from lib.d import D
from db.db import db
from forms.Produccion import ProduccionForm
from datetime import datetime, timedelta
from sqlalchemy import cast, Date
from models.Galleta_materia import Galleta_materia
from lib.security import safe
   

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
    ingredientes_dict = get_materia_dict()
    inventario_update = []
    for lote in inventario:
        inventario_data = lote.serialize()
        inventario_data['nombreMateria'] = ingredientes_dict.get(lote.id, 'Nombre no encontrado')
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
    materia = []
    for _lote in inventario_update:
        mp_selected = MateriaPrima.query.get(_lote['id_materia_prima'])
        materia.append(mp_selected)

    if request.method == 'POST':
        if 'add_galleta' in request.form:
            nombre_galleta = request.form.get('tipo_galleta')
            cantidad_prod = safe(request.form.get('cantidad_prod'))
            cantidad_prod = int(cantidad_prod)*10
            produccion_id = safe(request.form.get('id_produccion'))
            fecha_hoy = datetime.now()
            fecha_caducidad = fecha_hoy + timedelta(days=20)
            fecha_caducidad_date = fecha_caducidad.date()
            galleta = Galletas.query.filter_by(nombre = nombre_galleta).first()
            produccion_filter = Produccion.query.get(produccion_id)
            solicitud_filter = solicitud_produccion.query.get(produccion_filter.idSolicitud)

            #-------------------- Verificar no exceder la cantidad en la solicitud

            simulacion_cantidad = int(cantidad_prod) + produccion_filter.produccionActual
            if simulacion_cantidad > solicitud_filter.cantidad:
                flash("Cantidad excede la produccion solicitada")
                return redirect('/produccion')

            # ------------------- Verificar inventario --------------------

            total = 0
            ingredientes = Ingredientes.query.filter_by(galleta_id = galleta.id).all()
            for ingrediente in ingredientes:
                cantidad_requerida = ingrediente.cantidad * int(cantidad_prod)
                lotes_materia = InventarioMP.query.filter_by(id_materia_prima = ingrediente.material_id, estatus = 1).all()
                if lotes_materia:
                    for lote_materia in lotes_materia:
                        total += int(lote_materia.cantidad)
                    if total < cantidad_requerida:
                        more_mp = MateriaPrima.query.get(ingrediente.material_id)
                        flash(str("No hay suficientes insumos de " + more_mp.material))
                        return redirect('/produccion')
                else:
                    not_found_mp = MateriaPrima.query.get(ingrediente.material_id)
                    flash(str(not_found_mp.material + " no se encuentra en inventario"))
                    return redirect('/produccion')
                
            # -------------------- Agregar galleta ------------------

            inventario_activo = Inventario_galletas.query.filter_by(idGalleta=galleta.id, estatus = 1).first()
            if inventario_activo:
                total = inventario_activo.cantidad + int(cantidad_prod)
                inventario_activo.cantidad = total
                inventario_activo.updated_at = datetime.now()
                db.session.commit()
            else:
                inventario_insert = Inventario_galletas(
                    idGalleta = galleta.id,
                    cantidad = cantidad_prod,
                    estatus = 1,
                    fechaCaducidad = fecha_caducidad
                )
                db.session.add(inventario_insert)
                db.session.commit()

            # -------------------- Produccion -----------------------------------------
            if simulacion_cantidad == solicitud_filter.cantidad:
                produccion_filter.estatus = 1
            produccion_filter.produccionActual = simulacion_cantidad
            produccion_filter.updated_at = datetime.now()
            db.session.commit()

            # --------------------- Descontar inventario ----------------------------- 
            for ingrediente in ingredientes:
                cantidad_requerida = int(ingrediente.cantidad) * int(cantidad_prod)
                lotes_materia = InventarioMP.query.filter_by(id_materia_prima = ingrediente.material_id, estatus = 1).order_by(InventarioMP.caducidad.asc()).all()
                inventario_active = Inventario_galletas.query.filter_by(idGalleta=galleta.id, estatus = 1).first()
                print(inventario_active.idLoteGalletas)
                for lote in lotes_materia:
                    galleta_materia = Galleta_materia.query.filter_by(idLoteGalletas = inventario_active.idLoteGalletas, idLoteMateria = lote.id).first()
                    if int(lote.cantidad) < int(cantidad_requerida):
                        cantidad_requerida = int(cantidad_requerida) - int(lote.cantidad)
                        lote.cantidad = 0
                        lote.updated_at = datetime.now()
                        db.session.commit()
                        if not galleta_materia:
                            relacion = Galleta_materia(
                                idLoteMateria = lote.id,
                                idLoteGalletas = inventario_active.idLoteGalletas
                            )
                            db.session.add(relacion)
                            db.session.commit()
                    else:
                        materia_restante = int(lote.cantidad) - cantidad_requerida
                        lote.cantidad = materia_restante
                        lote.updated_at = datetime.now()
                        db.session.commit()
                        if not galleta_materia:
                            relacion = Galleta_materia(
                                idLoteMateria = lote.id,
                                idLoteGalletas = inventario_active.idLoteGalletas
                            )
                            db.session.add(relacion)
                            db.session.commit()
                        break
            flash("Galletas agregadas correctamente")
            return(redirect("/produccion"))
        elif 'add_merma' in request.form:
            produccion_id = safe(request.form.get('id_produccion'))
            ingrediente_merma = request.form.get('ingrediente')
            cantidad_merma = safe(request.form.get('cantidadIngrediente'))
            total = 0

            # -------------- Verificar existencia en inventario ----------------

            lotes_materia = InventarioMP.query.filter_by(id_materia_prima = ingrediente_merma, estatus = 1).all()
            if lotes_materia:
                for lote_materia in lotes_materia:
                    total += int(lote_materia.cantidad)
                if total < int(cantidad_merma):
                    more_mp = MateriaPrima.query.get(ingrediente_merma)
                    flash(str("No hay suficientes insumos de " + more_mp.material))
                    return redirect('/produccion')
            else:
                not_found_mp = MateriaPrima.query.get(ingrediente_merma)
                flash(str(not_found_mp.material + " no se encuentra en inventario"))
                return redirect('/produccion')

            # ---------------- Agregar a merma y descontar inventario------------------------------
            for lote_materia in lotes_materia:
                canitdad = 0
                if int(lote_materia.cantidad) < int(cantidad_merma):
                    cantidad = lote_materia.cantidad
                    inventario_merma = InventarioMP.query.get(lote_materia.id)
                    inventario_merma.cantidad = 0
                    db.session.commit()
                    cantidad_merma = int(cantidad_merma) - int(lote_materia.cantidad)

                    merma_materia =MermaMateria(
                        idInventarioMaterias = lote_materia.id,
                        merma_tipo = "Produccion",
                        merma_fecha = lote_materia.caducidad,
                        cantidad = cantidad,
                        created_at = datetime.now(),
                        id_produccion = produccion_id,
                        justificacion = "Produccion"
                    )
                    db.session.add(merma_materia)
                    db.session.commit()
                    flash("Algo salió mal")
                else:
                    cantidad = cantidad_merma
                    inventario_merma = InventarioMP.query.get(lote_materia.id)
                    inventario_merma.cantidad = int(lote_materia.cantidad) - int(cantidad_merma)
                    db.session.commit()
                    merma_materia =MermaMateria(
                        idInventarioMaterias = lote_materia.id,
                        merma_tipo = "Produccion",
                        merma_fecha = lote_materia.caducidad,
                        cantidad = cantidad,
                        created_at = datetime.now(),
                        id_produccion = produccion_id,
                        justificacion = "Produccion"
                    )
                    db.session.add(merma_materia)
                    db.session.commit()
                    flash("Merma agregada correctamente")
                    return(redirect("/produccion"))
        elif 'finalizar' in request.form:
            produccion_id = safe(request.form.get('id_produccion'))
            produccion_fin = Produccion.query.get(produccion_id)
            produccion_fin.estatus = 1
            db.session.commit()  
            if produccion_fin.produccionActual == 0:
                solicitud_rest = solicitud_produccion.query.get(produccion_fin.idSolicitud)
                lote_rest = Inventario_galletas.query.get(solicitud_rest.idLoteGalletas)
                lote_rest.estatus = 1
                db.session.commit()
            flash("Solicitud finalizada")
            return(redirect('/produccion'))

    return render_template('pages/produccion/index.html', solicitud=solicitud, form=form, produccion = produccion_filtro, inventario = inventario_update, materia = materia)
        
def calcular_materia_prima_restante(nombre):
    producciones_activas = Produccion.query.filter_by(estatus=0).all()
    materia_prima_necesaria = {}

    for produccion in producciones_activas:
        solicitud = solicitud_produccion.query.get(produccion.idSolicitud)
        galletas_restantes = solicitud.cantidad - produccion.produccionActual
        galleta = Galletas.query.filter_by(nombre = nombre).first()
        ingredientes = Ingredientes.query.filter_by(galleta_id=galleta.id).all()

        for ingrediente in ingredientes:
            cantidad_requerida_total = galletas_restantes * ingrediente.cantidad

            if ingrediente.material_id in materia_prima_necesaria:
                materia_prima_necesaria[ingrediente.material_id] += cantidad_requerida_total
            else:
                materia_prima_necesaria[ingrediente.material_id] = cantidad_requerida_total

    return materia_prima_necesaria
                

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
            solicitud_id = safe(request.form.get('solicitud_id'))
            nombre_galleta = request.form.get('nombreGalleta')
            mp_requerida_prod = calcular_materia_prima_restante(nombre_galleta)
            total = 0
            galleta = Galletas.query.filter_by(nombre = nombre_galleta).first()
            ingredientes = Ingredientes.query.filter_by(galleta_id = galleta.id).all()
            solicitud_filter = solicitud_produccion.query.get(solicitud_id)
            for ingrediente in ingredientes:
                cantidad_requerida = ingrediente.cantidad * int(solicitud_filter.cantidad)
                if mp_requerida_prod:
                    material_prod = mp_requerida_prod[ingrediente.material_id]
                    cantidad_requerida = cantidad_requerida + material_prod
                lotes_materia = InventarioMP.query.filter_by(id_materia_prima = ingrediente.material_id, estatus = 1).all()
                if lotes_materia:
                    for lote_materia in lotes_materia:
                        total += int(lote_materia.cantidad)
                    if total < cantidad_requerida:
                        more_mp = MateriaPrima.query.get(ingrediente.material_id)
                        flash(str("No hay suficientes insumos de " + more_mp.material))
                        return redirect(url_for('produccion.revisar_solicitudes'))
                else:
                    not_found_mp = MateriaPrima.query.get(ingrediente.material_id)
                    flash(str(not_found_mp.material + " no se encuentra en inventario"))
                    return redirect('/revisar_solicitudes')
            solicitud_filter.estatus = 'Aceptada'
            solicitud_filter.updated_at = datetime.now()
            db.session.commit()
            produccion = Produccion(
                idSolicitud = solicitud_id,
                idUsuario = 1
            )
            db.session.add(produccion)
            db.session.commit()
            flash("Solicitud aceptada")
            return redirect('/revisar_solicitudes')
            #return redirect(url_for('produccion.revisar_solicitudes'))
        elif 'rechazada' in request.form:
            justificacion_text = safe(request.form['justificacion'])  # Extraer el texto de justificación del formulario
            if justificacion_text == "":
                flash("Por favor, agrega una justificación")
                return redirect('/revisar_solicitudes')
            solicitud_id = request.form.get('reject_solicitud_id')
            solicitud = solicitud_produccion.query.get(solicitud_id)
            if solicitud:  # Verificar que el registro exista
                solicitud.justificacion = justificacion_text  # Actualizar la justificación
                solicitud.estatus = 'Rechazada'  # Cambiar el estatus a 'Rechazado'
                solicitud.updated_at = datetime.now()
                db.session.commit()  # Guardar los cambios en la base de datos
            inventario = Inventario_galletas.query.get(solicitud.idLoteGalletas)
            if inventario:
                inventario.estatus = 1
                inventario.updated_at = datetime.now()
                db.session.commit()
            return redirect('/revisar_solicitudes')
    return render_template('pages/produccion/show.html', solicitud=solicitues_filtro, galletas = galletas)