from flask import Blueprint, render_template, request, flash, redirect, g
from sqlalchemy import extract
from forms.VentaForm import VentaForm
from models.corte_diario import CorteDiario
from models.venta import Venta
from models.usuario import Usuario
from models.Recetas import Galletas
from forms.DetalleVentaForm import DetalleVentaForm
from models.detalleVenta import DetalleVenta
from models.Inventario_galletas import Inventario_galletas
from datetime import datetime
from db.db import db
from lib.jwt import token_required, allowed_roles, createToken, decodeToken
from lib.d import D

log = D(debug=True)

ventas = Blueprint("ventas", __name__, template_folder="templates")

@ventas.route("/ventas", methods=["GET", "POST"])
@token_required
@allowed_roles(roles=["admin", "ventas"])
def index():
    try:
        token = decodeToken(request.cookies.get("token"))
    except:
        token = None

    if not token:
        return redirect("/login")
    try:
        email = token["email"]
        idUsuario = Usuario.query.filter_by(email=email).first().id
    except Exception as e:
        flash(f"Error al obtener el Usuario", "error")
        return redirect("/venta")
        
    form = VentaForm()
    form.idUsuario.data = str(idUsuario)

    total = 0
    if request.method == "POST":
        fecha_venta = datetime.now().date()
        try:
            if request.form.get('btn') == "Crear":
                form.total.data = total

                if form.total.data is None:
                    flash("El campo total no puede estar vacío", "error")
                    return redirect("/ventas")
                
                venta = Venta(
                    idUsuario=form.idUsuario.data,
                    total=form.total.data,
                    fecha_venta= fecha_venta,
                    created_at=datetime.now()
                )
            
                db.session.add(venta)
                db.session.commit()

                flash("Venta creada correctamente", "success")
                lista_ventas.clear()
                return redirect("/venta")   
            
            elif request.form.get('btn') == "Corte":
                if form.total.data is None:
                    flash("El campo total no puede estar vacío", "error")
                    return redirect("/ventas")
                
                fecha_filtrar = datetime.strptime(fecha_venta.strftime("%Y-%m-%d"), "%Y-%m-%d")
                #fecha_filtrar = datetime.strptime("2024-04-13", "%Y-%m-%d")

                log.info(f"Fecha a filtrar: {fecha_filtrar}")

                # Extraemos el día, mes y año de la fecha a filtrar
                dia = fecha_filtrar.day
                mes = fecha_filtrar.month
                año = fecha_filtrar.year

                # Filtrar las ventas por el día, mes y año específicos
                ventas = Venta.query.filter(
                    extract('day', Venta.fecha_venta) == dia,
                    extract('month', Venta.fecha_venta) == mes,
                    extract('year', Venta.fecha_venta) == año,
                    Venta.idUsuario == idUsuario
                ).all()

                
                total = sum(venta.total for venta in ventas)
                totalSalida = 0
                
                corte_diario = CorteDiario(
                    fecha=fecha_venta,
                    totalEntrada=total,
                    totalSalida=totalSalida,
                    totalEfectivo=total-totalSalida,
                )

                db.session.add(corte_diario)
                db.session.commit()
                
                log.info(f"Total: {total}")
            
                return render_template("pages/venta/ventas.html", ventas=ventas, total=total, fecha=fecha_venta, form=form)
        except Exception as e:
            flash(f"Error al procesar la solicitud", "error")
            return redirect("/ventas")

    return render_template("pages/venta/ventas.html", form=form, total=total)

lista_ventas = []
@ventas.route("/venta", methods=["GET", "POST"])
@token_required
@allowed_roles(roles=["admin", "ventas"])
def detalle_venta():

    global lista_ventas
    try:
        token = decodeToken(request.cookies.get("token"))
    except:
        token = None
    if not token:
        return redirect("/login")
    
    try:
        email = token["email"]
        idUsuario = Usuario.query.filter_by(email=email).first().id
    except Exception as e:
        flash(f"Error al obtener el Usuario", "error")
        return redirect("/venta")
    
    form = VentaForm()
    form.idUsuario.data = str(idUsuario)
    total = 0

    tipo_venta = {
        1: 'Paquete 1kg',
        2: 'Paquete 700g',
        3: 'Unidad'
    }

    # Cargar diccionarios con el gramaje, el nombre, id y precios de las galletas
    gramaje = {}

    for galleta in Galletas.query.filter(Galletas.enable == 1).all():
        gramaje[galleta.id] = float(galleta.pesoGalleta)

    galletas = {}
    for galleta in Galletas.query.filter(Galletas.enable == 1).all():
        galletas[galleta.id] = galleta.nombre

    precios = {}
    for galleta in Galletas.query.filter(Galletas.enable == 1).all():
        precios[galleta.id] = float(galleta.precio)

    form2 = DetalleVentaForm()

    if request.method == "POST":
        try:    
            form2.process(request.form)
            log.warning(f"Form2: {request.form}")
            tvs = tipo_venta[int(form2.tipoVenta.data)]
            gs = galletas[int(form2.galleta_id.data)]
            log.warning(f"gs: {gs}")
            log.warning(f"tvs: {tvs}")

            inventario_galletas = db.session.query(Inventario_galletas).filter_by(idGalleta=int(form2.galleta_id.data)).first().cantidad

            if request.form['btn'] == 'Añadir':
                try:
                    cantidad_requerida = int(form2.cantidad.data)
                    galleta_id = int(form2.galleta_id.data)    
                
                    if form2.tipoVenta.data == "1" or  form2.tipoVenta.data == "2":  # Tipo de venta 1 o 2 (paquete 1kg o 700g)
                        
                        if form2.tipoVenta.data == "2": #Obtener la cantidad de galletas en base al gramaje
                            cantidad_galletas = ((cantidad_requerida * 700) / gramaje[galleta_id]) 
    
                        else:
                            cantidad_galletas = ((cantidad_requerida * 1000) / gramaje[galleta_id])
                        
                        if cantidad_galletas % 1 != 0:  #redondear la cantidad de galletas a un entero
                            cantidad_galletas = int(cantidad_galletas)

                        log.info(f"cantidad_galletas: {cantidad_galletas}")
                        log.info(f"cantidad_requerida: {cantidad_requerida}")
                        log.info(f"galletas en inventario: {inventario_galletas}")

                        if cantidad_galletas > inventario_galletas: #Validar si hay suficiente stock
                            flash("No hay suficiente stock disponible", "danger")
                            return redirect("/venta")
                        
                        for venta in lista_ventas: #Validar si ya se ha añadido el producto a la lista
                            if venta['galleta_id'] == galleta_id: 
                                if (venta['cantidad'] + cantidad_requerida) > inventario_galletas: #Validar si hay suficiente stock
                                    flash("No se puede agregar más de este producto, no hay suficiente stock disponible", "danger")
                                    return redirect("/venta")
                                else: #Si ya se ha añadido el producto, se hace otra venta diferente con la misma galleta
                                    
                                    venta_nueva = {
                                        'galleta_id': galleta_id,
                                        'galleta': gs,
                                        'cantidad': cantidad_requerida,
                                        'precio_unitario': form2.precio_unitario.data,
                                        'tipoVenta': tvs,
                                        'cantidad_galletas': cantidad_galletas,
                                    }

                                    lista_ventas.append(venta_nueva)
                                    break
                        else:  
                            venta_nueva = {
                                'galleta_id': galleta_id,
                                'galleta': gs,
                                'cantidad': cantidad_requerida,
                                'precio_unitario': form2.precio_unitario.data,
                                'tipoVenta': tvs,
                                'cantidad_galletas': cantidad_galletas,
                            }

                            lista_ventas.append(venta_nueva)
                            flash("Producto añadido correctamente", "success")
                        
                    else:
                        cantidad_galletas = cantidad_requerida  
                        
                        if cantidad_requerida > inventario_galletas:
                            flash("No hay suficiente stock disponible", "danger")
                            return redirect("/venta")
                        
                        for venta in lista_ventas:
                            if venta['galleta_id'] == galleta_id:
                                if (venta['cantidad'] + cantidad_requerida) > inventario_galletas:
                                    flash("No se puede agregar más de este producto, no hay suficiente stock disponible", "danger")
                                    return redirect("/venta")
                                else:
                                    venta['cantidad'] += cantidad_requerida
                                    flash("Producto añadido correctamente", "success")
                                    break
                        else:  
                            venta_nueva = {
                                'galleta_id': galleta_id,
                                'galleta': gs,
                                'cantidad': cantidad_requerida,
                                'precio_unitario': form2.precio_unitario.data,
                                'tipoVenta': tvs ,
                                'cantidad_galletas': cantidad_galletas,
                            }
                            
                            lista_ventas.append(venta_nueva)

                    total = sum(venta['cantidad'] * venta['precio_unitario'] for venta in lista_ventas)
                    form.total.data = total
                    
                    # volver a los valores por defecto de los campos
                    form2.cantidad.data = 1
                    form2.tipoVenta.data = "3"   

                except Exception as e:
                    flash(f"Error al añadir un producto a la lista", "error")
                    return redirect("/venta")

            if 'btn' in request.form and request.form['btn'].startswith("Eliminar"):
                try:
                    # Obtener el ID de la galleta desde el nombre del botón
                    galleta_id = int(request.form['eliminar'])

                    # Eliminar la producto correspondiente de la lista
                    for venta in lista_ventas:
                        if venta['galleta_id'] == galleta_id:
                            lista_ventas.remove(venta)
                            flash("Producto eliminado correctamente", "success")
                            break

                    total = sum(venta['cantidad'] * venta['precio_unitario'] for venta in lista_ventas)
                    form.total.data = total

                except Exception as e:
                    flash(f"Error al procesar la eliminacion", "error")
                    return redirect("/venta")

            if request.form['btn'] == "Vender":
                    if len(lista_ventas) == 0:
                        flash("No se puede vender sin productos", "danger")
                        return redirect("/venta")
                    else:
                        venta_id = Venta.query.order_by(Venta.id.desc()).first().id
                        cantidad_galletas = 0


                        log.info(f"Lista de ventas: {lista_ventas}")

                        log.info(f"inventario_galletas antes de actualizar: {inventario_galletas}")

                        for venta in lista_ventas:
                            detalle_venta = DetalleVenta(
                                venta_id=venta_id,
                                galleta_id=venta['galleta_id'],
                                cantidad=venta['cantidad'],
                                precio_unitario=venta['precio_unitario'],
                                created_at=datetime.now(),
                                tipoVenta=int(form2.tipoVenta.data)
                            )
                            db.session.add(detalle_venta)

                            galletas = db.session.query(Inventario_galletas).filter_by(idGalleta=venta['galleta_id']).first()
                            log.info(f"la cantidad de galletas en el inventario es: {galletas.cantidad}")
                             
                            new_cantidad = galletas.cantidad - venta['cantidad_galletas']

                            log.info(f"new_cantidad: {new_cantidad}")
                            
                            if new_cantidad < 0:
                                flash("No hay suficiente stock disponible", "danger")
                                return redirect("/venta")
                            else:
                                db.session.query(Inventario_galletas).filter_by(idGalleta=detalle_venta.galleta_id).update({'cantidad': new_cantidad, 'updated_at': datetime.now()})

                            # imprimir la cantidad de galletas en el inventario actual
                            log.info(f"Inventario de galletas actualizado: {inventario_galletas}")

                            total = sum(venta['cantidad'] * venta['precio_unitario'] for venta in lista_ventas)
                            form.total.data = total

                        db.session.query(Venta).filter_by(id=venta_id).update({'total': total})
                        
                        db.session.commit()
                        lista_ventas.clear()

                        flash("Venta creada correctamente", "success")
                        response = redirect("/createPdf")
                        response.set_cookie("venta_id", str(venta_id))
                        return response

            if request.form['btn'] == "Limpiar":
                try:
                    lista_ventas.clear()
                    flash("Lista vaciada con exito", "success")
                    return redirect("/venta")
                except Exception as e:
                    flash(f"Error al procesar la Cancelacion", "error")
                    return redirect("/venta")
            
            return render_template("pages/venta/index.html", form=form, form2=form2, lista_ventas=lista_ventas, total=total, inventario_galletas=inventario_galletas, galletas=galletas, precios=precios, gramaje=gramaje)

        except KeyError as e:
            flash("Error al procesar la solicitud", "error")
            return redirect("/venta")
        
        except Exception as e:
            flash(f"Error al procesar la solicitud", "error")
            return redirect("/venta")

    return render_template("pages/venta/index.html", form=form, form2=form2, lista_ventas=lista_ventas, total=total, galletas=galletas, precios=precios, gramaje=gramaje)

@ventas.route("/createPdf", methods=["GET", "POST"])
@token_required
@allowed_roles(roles=["admin", "ventas"])
def create_pdf():
    try:
        #si no hay el cookie venta_id redirigir a ventas
        if not request.cookies.get("venta_id"):
            return redirect("/venta")

        if request.method == "DELETE":
            #limpiar lista de galletas
            lista_ventas.clear()
            redire = redirect("/venta")
            redire.set_cookie("venta_id", "", expires=0)
            #cambiar el method a get
            redire.method = "GET"

            return redire

        galletas = {}
        for galleta in Galletas.query.all():
            galletas[galleta.id] = galleta.nombre
                
        tipo_venta = {
            '1': 'Paquete 1kg',
            '2': 'Paquete 700g',
            '3': 'Unidad'
        }

        token = decodeToken(request.cookies.get("token"))
        if not token:
            return redirect("/login")
        
        venta_id = request.cookies.get("venta_id")
        venta = Venta.query.filter_by(id=venta_id).first()

        detalle_venta = DetalleVenta.query.filter_by(venta_id=venta_id).all()

        detalle_venta = [detalle.serialize() for detalle in detalle_venta]

        # Modificar la estructura de detalle_venta
        detalles_venta = []
        total_venta = 0
        for detalle in detalle_venta:
            # log.info(f"Detalle: {detalle}")
            # log.warning(f"tipoVenta: {tipo_venta[detalle['tipoVenta']]}")
            detalle_modificado = {
                'galleta': galletas[detalle['galleta_id']],
                'tipoVenta': tipo_venta[detalle['tipoVenta']],
                'cantidad': detalle['cantidad'],
                'precio_unitario': detalle['precio_unitario']
            }
            detalles_venta.append(detalle_modificado)
        
            subtotal_detalle = float(detalle['cantidad']) * float(detalle['precio_unitario'])  
            total_venta += subtotal_detalle

        usuario = Usuario.query.filter_by(id=venta.idUsuario).first()

        # Renderizar el template y pasar los datos al contexto
        return render_template("pages/venta/createPdf.html", venta=venta, detalles_venta=detalles_venta, usuario=usuario, total_venta=total_venta)

    except Exception as e:
        flash(f"Error al procesar la solicitud {e}", "error")
        return redirect("/venta")
    
@ventas.route('/corteDiario', methods=['GET', 'POST'])
@token_required
@allowed_roles(roles=['admin', 'ventas'])
def corte_diario_index():
    try:
        token = decodeToken(request.cookies.get("token"))
    except:
        token = None

    if not token:
        return redirect('/login')
    
    email = token["email"]


    if request.method == "POST":
        fecha = request.form.get("fecha")
        # Convertir la fecha de cadena a objeto datetime
        fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
        print(f"Fecha: {fecha}")
        # Filtrar las ventas por la fecha seleccionada
        ventas = Venta.query.filter_by(idUsuario=Usuario.query.filter_by(email=email).first().id)\
                            .filter_by(fecha_venta=fecha).all()

        # Calcular el total de ventas para la fecha seleccionada
        total = sum(venta.total for venta in ventas)
        
        return render_template("pages/venta/corteDiario.html", ventas=ventas, total=total, fecha=fecha)

    return render_template("pages/venta/corteDiario.html")