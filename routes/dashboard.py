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
                 SELECT g.nombre, SUM(ig.cantidad) AS total_cantidad
FROM inventariogalletas ig
JOIN galletas g ON g.id = ig.idGalleta
WHERE g.enable = 1
GROUP BY g.nombre;

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
        min(totalGalletas) * COALESCE(SUM(costo_produccion) / min(totalGalletas), 0) as costoTotal, min(nombre) as nombre,min(precioTotal) as precioTotal
        FROM (
    SELECT
        nombre_material,
        SUM(cantidad_utilizada * precio_material) AS costo_produccion,
        totalGalletas AS totalGalletas,
        precioTotal as precioTotal,
        nombre
    FROM (
        SELECT
            mp.material AS nombre_material,
            SUM(i.cantidad) AS cantidad_utilizada,
            ROUND((SUM(mpp.cantidad)  * AVG(mpp.precio)), 2)/ 10000 AS precio_material,
            g.totalGalletas,
            g.nombre nombre,
            g.precio as precioTotal
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
        nombre_material, nombre, totalGalletas, precioTotal
    ) AS materiales;
    """)
    result = db.session.execute(query, {'id': id}).fetchone()
    
    return {
        'nombre': result[3] if result is not None else 'No disponible',
        'costoUnitario': str(result[0]) if result is not None else 0,
        'totalGalletas': str(result[1]) if result is not None else 0,
        'costoTotal': str(result[2]) if result is not None else 0,
        'precioTotal': str(result[4]) if result is not None else 0
    }



def get_id_galleta():
    query = text("""
        SELECT id FROM galletas WHERE enable = 1;
    """)
    result = db.session.execute(query).fetchall()
    return result

import datetime
def get_ventas_between_dates(str_inicio = datetime.datetime.now().strftime('%Y-%m-%d'), str_fin = datetime.datetime.now().strftime('%Y-%m-%d')):

    if str_inicio == '' or str_fin == '':
        str_inicio = datetime.datetime.now().strftime('%Y-%m-%d')
        str_fin = datetime.datetime.now().strftime('%Y-%m-%d')


    inicio = datetime.datetime.strptime(str_inicio, '%Y-%m-%d')
    fin = datetime.datetime.strptime(str_fin, '%Y-%m-%d')

    query = text("""
                 
SELECT 
    venta.id,
    venta.fecha_venta,
    venta.total,
    usuario.nombre,
    usuario.apellido

 FROM venta join usuario on venta.idUsuario = usuario.id WHERE fecha_venta BETWEEN :inicio AND :fin and total > 0 ORDER BY fecha_venta DESC;
    """)

    result = db.session.execute(query, {'inicio': inicio, 'fin': fin}).fetchall()


    log.warning(f"Inicio: {inicio}, Fin: {fin}, la query es: {query}, el resultado es: {result}")
    log.warning(f"ayuda: {result}")
    return [{'id': x[0], 'fecha_venta': x[1], 'total': x[2], 'nombre': x[3], 'apellido': x[4]} for x in result]



def get_all_costos_produccion():
    id_galletas = get_id_galleta()
    costos_produccion = []
    for id in id_galletas:
        costo_produccion = get_precio_produccion_by_id(id[0])
        if costo_produccion is not None:
            #agrergar el id de la galleta
            costos_produccion.append({'id': id[0], 'nombre': costo_produccion['nombre'], 'costoUnitario': costo_produccion['costoUnitario'], 'totalGalletas': costo_produccion['totalGalletas'], 'costoTotal': costo_produccion['costoTotal'], 'precioTotal': costo_produccion['precioTotal']})

    #eliminar del objeto los valores que no se necesitan si el nombre es null
    costos_produccion = [x for x in costos_produccion if x['totalGalletas'] != "None"]
    #convertir a costo unitario a float y redondear a 2 decimales y total de galletas a int
    for costo in costos_produccion:
        costo['costoUnitario'] = round(float(costo['costoUnitario']), 2)
        costo['totalGalletas'] = int(costo['totalGalletas'])
        costo['costoTotal'] = round(float(costo['costoTotal']), 2)
        costo['precioTotal'] = round(float(costo['precioTotal']), 2)

    return costos_produccion

def get_ids_produccion():
    ids = Produccion.query.with_entities(Produccion.idProduccion, Produccion.idUsuario).all()
    # Crear una lista de tuplas (idProduccion, idUsuario)
    lista_ids_produccion = []
    for id in ids:
        lista_ids_produccion.append({'id': id[0], 'idUsuario': id[1]})
    return lista_ids_produccion

def get_proveedor_by_produccion(id):
    query = text("""
        SELECT inventariogalletas.idLoteGalletas, proveedor.nombre_empresa, proveedor.nombre_encargado, proveedor.telefono_empresa, proveedor.direccion_empresa, proveedor.id
        FROM inventariogalletas
        JOIN materia_prima_proveedor ON materia_prima_proveedor.materiaprima_id = inventariogalletas.idGalleta
        JOIN proveedor ON proveedor.id = materia_prima_proveedor.proveedor_id
        WHERE inventariogalletas.idLoteGalletas = :id AND proveedor.estatus = 1
        GROUP BY proveedor.nombre_empresa, proveedor.nombre_encargado, proveedor.telefono_empresa, proveedor.direccion_empresa, proveedor.id;
        """)
    result = db.session.execute(query, {'id': id}).all()

    return result


def get_materiales_produccion_proveedor(idLote, idProveedor):
    query = text("""
                 SELECT 
    mp.material, 
    mpp.precio, 
    mpp.cantidad, 
    mpp.tipo 
    FROM 
        inventariogalletas ig 
    JOIN 
        ingredientes i ON i.galleta_id = ig.idGalleta
    JOIN 
        materiaprima mp ON mp.id = i.material_id
    JOIN 
        materia_prima_proveedor mpp ON mpp.materiaprima_id = mp.id
    WHERE 
        ig.idLoteGalletas = :id
        AND mpp.proveedor_id = :idProveedor;
    """)
    result = db.session.execute(query, {'id': idLote, 'idProveedor': idProveedor}).fetchall()
    return [{'material': x[0], 'precio': x[1], 'cantidad': x[2], 'tipo': x[3]} for x in result]

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
@allowed_roles(['admin', 'ventas', 'produccion', 'compras'])
def index():
    ranking_cookies = get_ranking_cookies()
    json_ranking_cookies = json.dumps(ranking_cookies)
    json_mermas = json.dumps(get_ranking_mermas())
    galletas_en_inventario = json.dumps(get_inventario_galletas())
    costo_produccion_galletas = get_all_costos_produccion()
    

    lista_ids_produccion = get_ids_produccion()
    lista_nombres_empleados = []
    lista_ids_produccion_reales = []
    lista_proveedores = []

    for id in lista_ids_produccion:
        nombre_empleado = know_user_by_id(id['idUsuario'])
        proveedores = get_proveedor_by_produccion(id['id'])
        
        log.warning(id['id'])
        log.error(proveedores)

        # Manejar múltiples proveedores para un mismo ID de producción
        if proveedores:
            for proveedor in proveedores:
                log.success(f"id: {id['id']}, proveedorID: {proveedor[0]}")

                lista_proveedores.append({
                    'id': id['id'], 
                    'proveedor': {
                        'idLoteGalletas': proveedor[0],
                        'nombre_empresa': proveedor[1],
                        'nombre_encargado': proveedor[2],
                        'telefono_empresa': proveedor[3],
                        'direccion_empresa': proveedor[4],
                        'idProveedor': proveedor[5],
                        'materiales': get_materiales_produccion_proveedor(id['id'], proveedor[5])
                    },
                    
                })

        if nombre_empleado:
            lista_ids_produccion_reales.append(id)
            lista_nombres_empleados.append({'id': id['id'], 'nombre_empleado': nombre_empleado[0]})

    


    ventas = get_ventas_between_dates()



    if request.method == 'POST':
        inicio = request.form['inicio']
        fin = request.form['fin']
        if inicio == '' or fin == '':
            inicio = datetime.datetime.now().strftime('%Y-%m-%d') and fin == datetime.datetime.now().strftime('%Y-%m-%d')
        log.error(f"Fecha inicio: {inicio}, Fecha fin: {fin}")
        if inicio == '' or fin == '':
            inicio = None and fin == None
        ventas = get_ventas_between_dates(inicio, fin)


    total_ventas = 0
    for venta in ventas:
        total_ventas += venta['total']
    
    log.warning(f"Ventas: {ventas}")
    #hacer que ranking_cookies sea un string para que pueda ser renderizado en el template    
    return render_template('pages/dashboard/index.html',
                            galletas_en_inventario=galletas_en_inventario,
                            ranking_cookies=json_ranking_cookies,
                            ranking_mermas=json_mermas,
                            produccion_ids=lista_ids_produccion_reales,
                            lista_nombres_empleados=lista_nombres_empleados,
                            info_produccion=costo_produccion_galletas,
                            proveedores=lista_proveedores,
                            ventas=ventas,
                            total_ventas=total_ventas
                            )

