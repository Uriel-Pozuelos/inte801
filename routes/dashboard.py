from flask import Blueprint, request, render_template, flash
import json
from sqlalchemy import text
from db.db import db
from lib.d import D
from models.Inventario_galletas import Inventario_galletas

dashboard = Blueprint('dashboard', __name__)
log = D(debug=True)


def get_ranking_cookies():
    query = text("""
        SELECT g.nombre, SUM(dv.cantidad) as cantidad_vendida FROM detalleventa dv
        JOIN galletas g ON g.id = dv.galleta_id
        GROUP BY g.nombre
        ORDER BY cantidad_vendida DESC;
    """)
    results = db.session.execute(query)
    labels = []
    data = []
    backgroundColor = ['#FF6384', '#36A2EB', '#FFCE56', '#FF6384', '#36A2EB', '#FFCE56', '#FF6384', '#36A2EB', '#FFCE56', '#FF6384', '#36A2EB', '#FFCE56']
    borderColor = ['#FF6384', '#36A2EB', '#FFCE56', '#FF6384', '#36A2EB', '#FFCE56', '#FF6384', '#36A2EB', '#FFCE56', '#FF6384', '#36A2EB', '#FFCE56']
    bg_color_index = 0  # Para rotar los colores de fondo
    border_color_index = 0  # Para rotar los colores de borde

    for result in results:
        labels.append(result[0])  # Asumiendo que 'nombre' es el primer elemento seleccionado
        data.append(float(result[1])) # Asumiendo que 'cantidad_vendida' es el segundo elemento seleccionado
        
        # Añadir colores de manera cíclica para que no se agoten
        if bg_color_index >= len(backgroundColor):
            bg_color_index = 0
        if border_color_index >= len(borderColor):
            border_color_index = 0
        
        bg_color_index += 1
        border_color_index += 1

    return {
        'labels': labels,
        'datasets': [
            {
                'label': 'Ranking de galletas más vendidas',
                'data': data,
                'backgroundColor': backgroundColor * (len(data) // len(backgroundColor)) + backgroundColor[:len(data) % len(backgroundColor)],
                'borderColor': borderColor * (len(data) // len(borderColor)) + borderColor[:len(data) % len(borderColor)],
                'borderWidth': 1
            }
        ]
    }

def get_ranking_mermas():
    query = text("""
        SELECT g.nombre, SUM(m.cantidad) as cantidad_merma FROM merma_galletas m
        JOIN inventariogalletas ig ON ig.idLoteGalletas = m.idInventarioGalletas
        JOIN galletas g ON g.id = ig.idGalleta
        GROUP BY g.nombre
    """)
    results = db.session.execute(query)
    labels = []
    data = []
    backgroundColor = ['#FF6384', '#36A2EB', '#FFCE56', '#FF6384', '#36A2EB', '#FFCE56', '#FF6384', '#36A2EB', '#FFCE56', '#FF6384', '#36A2EB', '#FFCE56']
    borderColor = ['#FF6384', '#36A2EB', '#FFCE56', '#FF6384', '#36A2EB', '#FFCE56', '#FF6384', '#36A2EB', '#FFCE56', '#FF6384', '#36A2EB', '#FFCE56']
    bg_color_index = 0  # Para rotar los colores de fondo
    border_color_index = 0  # Para rotar los colores de borde

    for result in results:
        labels.append(result[0])
        data.append(float(result[1]))

        # Añadir colores de manera cíclica para que no se agoten
        if bg_color_index >= len(backgroundColor):
            bg_color_index = 0
        if border_color_index >= len(borderColor):
            border_color_index = 0

        bg_color_index += 1
        border_color_index += 1

    return {
        'labels': labels,
        'datasets': [
            {
                'label': 'Ranking de galletas con más merma',
                'data': data,
                'backgroundColor': backgroundColor * (len(data) // len(backgroundColor)) + backgroundColor[:len(data) % len(backgroundColor)],
                'borderColor': borderColor * (len(data) // len(borderColor)) + borderColor[:len(data) % len(borderColor)],
                'borderWidth': 1
            }
        ]
    }


def get_ids_produccion():
    ids = Inventario_galletas.query.with_entities(Inventario_galletas.idLoteGalletas).all()
    ids = [id[0] for id in ids]
    return ids

def know_user_by_id(id):
    query = text("""
        select concat(u.nombre, ' ', u.apellido) as nombre_empleado, ig.idLoteGalletas
        from inventariogalletas ig
        JOIN produccion p ON p.idSolicitud = ig.idLoteGalletas
        JOIN usuario u ON u.id = p.idUsuario
        WHERE ig.idLoteGalletas = :id;
    """)
    result = db.session.execute(query, {'id': id}).fetchone()
    return result



@dashboard.route('/dashboard', methods=['GET', 'POST'])
def index():
    ranking_cookies = get_ranking_cookies()
    json_ranking_cookies = json.dumps(ranking_cookies)
    json_mermas = json.dumps(get_ranking_mermas())
    lista_ids_produccion = get_ids_produccion()
    lista_nombres_empleados = []
    lista_ids_produccion_reales = []
    for id in lista_ids_produccion:
        nombre_empleado = know_user_by_id(id)
        if nombre_empleado is not None:
          lista_ids_produccion_reales.append(id)
          lista_nombres_empleados.append({'id': id, 'nombre': nombre_empleado[0]})
    log.info(lista_nombres_empleados)
    #hacer que ranking_cookies sea un string para que pueda ser renderizado en el template    
    return render_template('pages/dashboard/index.html',
                            ranking_cookies=json_ranking_cookies,
                            ranking_mermas=json_mermas,
                            produccion_ids=lista_ids_produccion_reales,
                            lista_nombres_empleados=lista_nombres_empleados)