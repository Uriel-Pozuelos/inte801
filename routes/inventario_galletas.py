from flask import Blueprint, request, render_template, redirect, url_for, flash
from models.Recetas import Galletas, MateriaPrima
from models.Inventario_galletas import Inventario_galletas
from models.merma_galletas import Merma_galletas
from lib.d import D
from db.db import db
from datetime import datetime, date
from lib.jwt import token_required, allowed_roles, createToken, decodeToken

inventario_galletas = Blueprint('inventario_galletas', __name__, template_folder='templates')
log = D(debug=True)

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

@inventario_galletas.route('/inventario_galletas', methods=['GET', 'POST'])
@token_required
@allowed_roles(roles=["admin", "ventas"])
def index():
    inventario = get_inventario_galletas()
    all_merma = Merma_galletas.query.all()
    
    ids_merma = []
    if all_merma:
        for merma in all_merma:
            ids_merma.append(merma.idInventarioGalletas)
    inventario_filter = []
    lote_caducado = []
    for lote in inventario:
        fecha_caducidad = lote['fechaCaducidad'].date()
        fecha_actual = date.today()
        if lote['idLoteGalletas'] not in ids_merma and not lote['cantidad'] == 0:
                inventario_filter.append(lote)
    for lote in inventario:
        fecha_caducidad = lote['fechaCaducidad'].date()
        fecha_actual = date.today()
        if all_merma:
            if fecha_caducidad <= fecha_actual and lote['idLoteGalletas'] not in ids_merma:
                lote_caducado.append(lote)

    if request.method == 'POST':
        tipo_merma = request.form.get('razonMerma')
        lote_seleccionado = request.form.get('lote')
        cantidad = request.form.get('cantidad')
        if not tipo_merma or not lote_seleccionado:
            flash('Completa todos los campos')
            return(redirect('/inventario_galletas'))
        cantidad = int(cantidad)
        
        if tipo_merma == 'Por caducidad':
            lote = Inventario_galletas.query.get(lote_seleccionado)
            add_merma = Merma_galletas(
                idInventarioGalletas = lote.idLoteGalletas,
                cantidad = lote.cantidad,
                fechaCaducidad = lote.fechaCaducidad,
                justificaion = "Caducidad"
            )
            db.session.add(add_merma)
            db.session.commit()
            lote.cantidad = 0
            db.session.commit()
            flash('La merma se agregó de forma correcta')
            return(redirect('/inventario_galletas'))
        elif tipo_merma == 'Galleta dañada':
            lote = Inventario_galletas.query.get(lote_seleccionado)
            if cantidad > int(lote.cantidad):
                flash('La cantidad que solicitas excede nuestro stock')
                return(redirect('/inventario_galletas'))
            
            add_merma = Merma_galletas(
                idInventarioGalletas = lote.idLoteGalletas,
                cantidad = cantidad,
                fechaCaducidad = lote.fechaCaducidad,
                justificaion = "Galleta dañada"
            )
            db.session.add(add_merma)
            db.session.commit()
            cantidad = cantidad - int(lote.cantidad)
            lote.cantidad = cantidad
            db.session.commit()
            flash('La merma se agregó de forma correcta')
            return(redirect('/inventario_galletas'))

    for lote in all_merma:
        inv_mermado = Inventario_galletas.query.get(lote.idInventarioGalletas)
        galleta = Galletas.query.get(inv_mermado.idGalleta)
        lote.nombreGalleta = galleta.nombre

    return render_template('pages/inventario_galletas/index.html', inventario = inventario_filter, caducado = lote_caducado, mermas = all_merma)