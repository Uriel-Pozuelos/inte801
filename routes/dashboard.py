from flask import Blueprint, request, render_template, flash
import json
from sqlalchemy import text
from db.db import db
from lib.d import D
from models.Inventario_galletas import Inventario_galletas
from models.Produccion import Produccion
from lib.jwt import allowed_roles,token_required
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

def get_inventario_galletas():
    query = text("""
                 SELECT g.nombre, ig.cantidad
                FROM inventariogalletas ig
                JOIN galletas g ON g.id = ig.idGalleta;
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
        data.append(int(result[1]))

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
                'label': 'Inventario de galletas',
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


def get_precio_produccion_by_id(id):
    query = text("""
       SELECT COALESCE(SUM(costo_produccion) / min(totalGalletas), 0) as costoUnitario, min(totalGalletas) ,
min(totalGalletas) * COALESCE(SUM(costo_produccion) / min(totalGalletas), 0) as costoTotal, min(nombre) as nombre
FROM (
    SELECT
        nombre_material,
        SUM(cantidad_utilizada * precio_material) AS costo_produccion,
        totalGalletas AS totalGalletas,
        nombre
    FROM (
        SELECT
            mp.material AS nombre_material,
            SUM(i.cantidad) AS cantidad_utilizada,
            ROUND((SUM(mpp.cantidad)/ 1000  * AVG(mpp.precio)), 2) AS precio_material,
            g.totalGalletas,
            g.nombre nombre
        FROM
            ingredientes i
        JOIN
            materiaprima mp ON i.material_id = mp.id
        JOIN
            galletas g ON i.galleta_id = g.id
		JOIN 
			materia_prima_proveedor mpp on mpp.materiaprima_id = mp.id
        WHERE
            g.id = :id and g.enable = 1
        GROUP BY
            mp.material, g.totalGalletas, g.precio, mpp.materiaprima_id, g.nombre
    ) AS materiales
    GROUP BY
        nombre_material, nombre
) AS p;
    """)
    result = db.session.execute(query, {'id': id}).fetchone()
    
    return {
        'nombre': result[3] if result is not None else 'No disponible',
        'costoUnitario': str(result[0]) if result is not None else 0,
        'totalGalletas': str(result[1]) if result is not None else 0,
        'costoTotal': str(result[2]) if result is not None else 0
    }


def get_id_galleta():
    query = text("""
        SELECT id FROM galletas WHERE enable = 1;
    """)
    result = db.session.execute(query).fetchall()
    return result

def get_all_costos_produccion():
    id_galletas = get_id_galleta()
    costos_produccion = []
    for id in id_galletas:
        costo_produccion = get_precio_produccion_by_id(id[0])
        if costo_produccion is not None:
            #agrergar el id de la galleta
            costos_produccion.append({'id': id[0], 'nombre': costo_produccion['nombre'], 'costoUnitario': costo_produccion['costoUnitario'], 'totalGalletas': costo_produccion['totalGalletas'], 'costoTotal': costo_produccion['costoTotal']})

    #eliminar del objeto los valores que no se necesitan si el nombre es null
    costos_produccion = [x for x in costos_produccion if x['totalGalletas'] != "None"]
    #convertir a costo unitario a float y redondear a 2 decimales y total de galletas a int
    for costo in costos_produccion:
        costo['costoUnitario'] = round(float(costo['costoUnitario']), 2)
        costo['totalGalletas'] = int(costo['totalGalletas'])
        costo['costoTotal'] = round(float(costo['costoTotal']), 2)

    return costos_produccion

def get_ids_produccion():
    ids = Produccion.query.with_entities(Produccion.idProduccion, Produccion.idUsuario).all()
    # Crear una lista de tuplas (idProduccion, idUsuario)
    lista_ids_produccion = []
    for id in ids:
        lista_ids_produccion.append({'id': id[0], 'idUsuario': id[1]})
    return lista_ids_produccion



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
@token_required
@allowed_roles(['admin', 'ventas', 'produccion'])
def index():
    ranking_cookies = get_ranking_cookies()
    json_ranking_cookies = json.dumps(ranking_cookies)
    json_mermas = json.dumps(get_ranking_mermas())
    galletas_en_inventario = json.dumps(get_inventario_galletas())
    costo_produccion_galletas = get_all_costos_produccion()
    log.json(costo_produccion_galletas)

    lista_ids_produccion = get_ids_produccion()
    lista_nombres_empleados = []
    lista_ids_produccion_reales = []
    for id in lista_ids_produccion:
        nombre_empleado = know_user_by_id(id['idUsuario'])
       
        if nombre_empleado is not None:
          lista_ids_produccion_reales.append(id)
          lista_nombres_empleados.append({'id': id['id'], 'nombre_empleado': nombre_empleado[0]})
    log.info(lista_nombres_empleados)
    #hacer que ranking_cookies sea un string para que pueda ser renderizado en el template    
    return render_template('pages/dashboard/index.html',
                            galletas_en_inventario=galletas_en_inventario,
                            ranking_cookies=json_ranking_cookies,
                            ranking_mermas=json_mermas,
                            produccion_ids=lista_ids_produccion_reales,
                            lista_nombres_empleados=lista_nombres_empleados,
                            info_produccion=costo_produccion_galletas
                            )

