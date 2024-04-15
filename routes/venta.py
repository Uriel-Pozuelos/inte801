from flask import Blueprint, render_template, request, flash, redirect, g
from forms.VentaForm import VentaForm
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

def index():
    galletas = Galletas.query.all()
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
        flash(f"Error al obtener el Usuario {e}", "error")
        return redirect("/venta")
        
    form = VentaForm()
    form.idUsuario.data = str(idUsuario)

    total = 0
    if request.method == "POST":
        try:
            if request.form['btn'] == "Agregar":
                # Agrega una validacion para que no se pueda agregar una venta si no se ha asociado a detalle venta
                
                venta = Venta(
                    idUsuario=form.idUsuario.data,
                    total=form.total.data,
                    fecha_venta=datetime.now(),
                    created_at=datetime.now()
                )
                db.session.add(venta)
                db.session.commit()
                flash("Venta creada correctamente", "success")
                lista_ventas.clear()
                return redirect("/ventas")      

            # if request.form['btn'] == 'Ver':
            #     form.venta_id.data = request.form['venta_id']
            #     detalle_venta = DetalleVenta.query.filter_by(venta_id=form.venta_id.data).all()
            #     for detalle in detalle_venta:
            #         total += detalle.cantidad * detalle.precio_unitario
            #     ventas = Venta.query.all()

            if request.form['btn'] == 'Filtrar':
                form.fecha.data = request.form['fecha']
                print(form.fecha.data)
                ventas = Venta.query.filter_by(fecha_venta=form.fecha.data).all()
                for venta in ventas:
                    total += venta.total
        
        except Exception as e:
            flash(f"Error al procesar la solicitud {e}", "error")
            return redirect("/ventas")

        return render_template("pages/venta/ventas.html", form=form, total=total )

    ventas = Venta.query.all()
    print(ventas)
    for venta in ventas:
        total += venta.total
    
    return render_template("pages/venta/ventas.html", form=form, ventas=ventas, total=total, galleta=galletas)

lista_ventas = []
@ventas.route("/venta", methods=["GET", "POST"])

def detalle_venta():

    global lista_ventas
    try:
        token = decodeToken(request.cookies.get("token"))
    except:
        token = None
    if not token:
        return redirect("/login")
    
    # agrega un try para manejar el error del idUsuario
    try:
        email = token["email"]
        idUsuario = Usuario.query.filter_by(email=email).first().id
    except Exception as e:
        flash(f"Error al obtener el Usuario {e}", "error")
        return redirect("/venta")
    
    form = VentaForm()
    form.idUsuario.data = str(idUsuario)
    total = 0

    tipo_venta = {
        1: 'Paquete 1kg',
        2: 'Paquete 700g',
        3: 'Unidad'
    }

    gramaje = {
        1: 45,
        2: 55,
        3: 50,
        4: 60,
        5: 48,
        6: 40,
        7: 52,
        8: 50,
        9: 58,
        10: 55
    }

    # Haz que el diccionario de galletas se cargue desde la base de datos
    galletas = {}
    for galleta in Galletas.query.all():
        galletas[galleta.id] = galleta.nombre

    print(galletas)

    
    form2 = DetalleVentaForm()

    if request.method == "POST":
        try:    
            form2.process(request.form)
            tvs = tipo_venta[int(form2.tipoVenta.data)]
            gs = galletas[int(form2.galleta_id.data)]

            inventario_galletas = db.session.query(Inventario_galletas).filter_by(idGalleta=int(form2.galleta_id.data)).first().cantidad

            if request.form['btn'] == 'Añadir':
                try:
                    cantidad_requerida = int(form2.cantidad.data)
                    galleta_id = int(form2.galleta_id.data)
                    print(tipo_venta)
                    
                    if form2.tipoVenta.data == "1" or  form2.tipoVenta.data == "2":  # Tipo de venta 1 o 2 (paquete 1kg o 700g)
                        
                        if form2.tipoVenta.data == 2: #Obtener la cantidad de galletas en base al gramaje
                            cantidad_galletas = ((cantidad_requerida * 700) / gramaje[galleta_id]) 
                        else:
                            cantidad_galletas = ((cantidad_requerida * 1000) / gramaje[galleta_id])
                        
                        if cantidad_galletas % 1 != 0:  #redondear la cantidad de galletas a un entero
                            cantidad_galletas = int(cantidad_galletas)
                            print(cantidad_galletas)  

                        if cantidad_galletas > inventario_galletas: #Validar si hay suficiente stock
                            flash("No hay suficiente stock disponible", "danger")
                            return redirect("/venta")
                        
                        for venta in lista_ventas: #Validar si ya se ha añadido el producto a la lista
                            if venta['galleta_id'] == galleta_id: 
                                if (venta['cantidad'] + cantidad_requerida) > inventario_galletas: #Validar si hay suficiente stock
                                    flash("No se puede agregar más de este producto, no hay suficiente stock disponible", "danger")
                                    return redirect("/venta")
                                else: #Si ya se ha añadido el producto, se hace otra venta diferente con la misma galleta
                                    
                                    break
                        else:  
                            venta_nueva = {
                                'galleta_id': galleta_id,
                                'cantidad': cantidad_requerida,
                                'precio_unitario': form2.precio_unitario.data,
                                'tipoVenta': form2.tipoVenta.data,
                                'cantidad_galletas': cantidad_galletas,
                            }
                            lista_ventas.append(venta_nueva)
                            flash("Producto añadido correctamente", "success")
                        print(lista_ventas)
                        
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
                                'cantidad': cantidad_requerida,
                                'precio_unitario': form2.precio_unitario.data,
                                'tipoVenta': form2.tipoVenta.data,
                                'cantidad_galletas': cantidad_galletas,
                            }
                            lista_ventas.append(venta_nueva)

                    total = sum(venta['cantidad'] * venta['precio_unitario'] for venta in lista_ventas)
                    form.total.data = total
                    print(lista_ventas)    

                except Exception as e:
                    flash(f"Error al añadir un producto a la lista {e}", "error")
                    return redirect("/venta")

            if 'btn' in request.form and request.form['btn'].startswith("Eliminar"):
                try:
                    # Obtener el ID de la galleta desde el nombre del botón
                    galleta_id = int(request.form['eliminar'])
                    print(galleta_id)

                    # Eliminar la venta correspondiente de la lista
                    for venta in lista_ventas:
                        if venta['galleta_id'] == galleta_id:
                            lista_ventas.remove(venta)
                            flash("Venta eliminada correctamente", "success")
                            break
                    log.info(f"Lista de ventas: {lista_ventas}")
                    total = sum(venta['cantidad'] * venta['precio_unitario'] for venta in lista_ventas)
                    form.total.data = total

                except Exception as e:
                    flash(f"Error al procesar la eliminacion {e}", "error")
                    return redirect("/venta")

            if request.form['btn'] == "Vender":
                try:
                    if len(lista_ventas) == 0:
                        flash("No se puede vender sin productos", "danger")
                        return redirect("/venta")
                    else:
                        venta_id = Venta.query.order_by(Venta.id.desc()).first().id
                        cantidad_galletas = 0
                        for venta in lista_ventas:
                            detalle_venta = DetalleVenta(
                                venta_id=venta_id,
                                galleta_id=venta['galleta_id'],
                                cantidad=venta['cantidad'],
                                precio_unitario=venta['precio_unitario'],
                                created_at=datetime.now(),
                                tipoVenta=venta['tipoVenta']
                            )
                            db.session.add(detalle_venta)
                            inventario_galletas = inventario_galletas - cantidad_galletas; 
                            db.session.query(Inventario_galletas).filter_by(idGalleta=detalle_venta.galleta_id).update({'cantidad': inventario_galletas, 'updated_at': datetime.now()})

                            total = sum(venta['cantidad'] * venta['precio_unitario'] for venta in lista_ventas)
                            form.total.data = total

                        print(detalle_venta)
                        print(cantidad_galletas)
                        print(detalle_venta.cantidad)
                        print(total)
                        db.session.query(Venta).filter_by(id=venta_id).update({'total': total})
                        
                        db.session.commit()
                        lista_ventas.clear()

                        flash("Venta creada correctamente", "success")
                        response = redirect("/createPdf")
                        response.set_cookie("venta_id", str(venta_id))
                        return response
                    
                except Exception as e:
                    flash(f"Error al procesar la Venta {e}", "error")
                    return redirect("/venta")

            if request.form['btn'] == "Cancelar":
                try:
                    lista_ventas.clear()
                    flash("Venta cancelada", "success")
                    return redirect("/venta")
                except Exception as e:
                    flash(f"Error al procesar la Cancelacion {e}", "error")
                    return redirect("/venta")
            
            print(galletas)
            return render_template("pages/venta/index.html", form=form, form2=form2, lista_ventas=lista_ventas, total=total, inventario_galletas=inventario_galletas, galletas=galletas)

        except KeyError as e:
            flash("Error al procesar la solicitud {e}", "error")
            return redirect("/venta")
        
        except Exception as e:
            flash(f"Error al procesar la solicitud {e}", "error")
            return redirect("/venta")

    return render_template("pages/venta/index.html", form=form, form2=form2, lista_ventas=lista_ventas, total=total, galletas=galletas)

@ventas.route("/createPdf", methods=["GET", "POST"])

def create_pdf():
    try:
        #si no hay el cookie venta_id redirigir a ventas
        if not request.cookies.get("venta_id"):
            return redirect("/venta")

        if request.method == "DELETE":
            #limpiar lista cookie
            lista_ventas.clear()
            log.info(f"Lista de ventas: {lista_ventas}")
            redire = redirect("/venta")
            redire.set_cookie("venta_id", "", expires=0)
            #cambiar el method a get
            redire.method = "GET"

            return redire


        galletas = {
            1: 'Galleta de avena',
            2: 'Galleta de chocolate',
            3: 'Galleta de azúcar',
            4: 'Galleta de Pasas y Nueces',
            5: 'Galleta de Limón y Coco',
            6: 'Galleta de Jengibre',
            7: 'Galleta de Especias',
            8: 'Galleta de Miel',
            9: 'Galleta de Chocolate y Coco',
            10: 'Galleta de Avena y Miel'
        }
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

        log.warning(detalle_venta)
        log.warning(venta.serialize())

        # Modificar la estructura de detalle_venta
        detalles_venta = []
        total_venta = 0
        for detalle in detalle_venta:
            log.info(f"Detalle: {detalle}")
            log.warning(f"tipoVenta: {tipo_venta[detalle['tipoVenta']]}")
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
    
@ventas.route('/corte_diario', methods=['GET'])

def corte_diario_index():
    try:
        token = decodeToken(request.cookies.get("token"))
    except:
        token = None

    if not token:
        return redirect('/login')
    
    email = token["email"]
    
    ventas = Venta.query.filter_by(usuario_id=Usuario.query.filter_by(email=email).first().id).all()
    
    total = 0
    for venta in ventas:
        total += venta.total
    return render_template("pages/venta/corteDiario.html", ventas=ventas, total=total)
