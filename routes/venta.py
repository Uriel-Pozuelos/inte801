from flask import Blueprint, render_template, request, flash, redirect, g
from forms.VentaForm import VentaForm
from models.venta import Venta
from models.usuario import Usuario
# from models.Galletas import Galletas
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
    

    
    email = token["email"]
    
    idUsuario = Usuario.query.filter_by(email=email).first().id 
    form = VentaForm()
    form.idUsuario.data = str(idUsuario)
    print(idUsuario)

    total = 0
    if request.method == "POST":
        print(request.form)
        
        if request.form['btn'] == "Agregar":
            venta = Venta(
                fecha_venta=datetime.now(),
                total=total,
                idUsuario=form.idUsuario.data,
                created_at=datetime.now()
            )
            print(request.form)
            db.session.add(venta)
            db.session.commit()
            flash("Venta creada correctamente", "success")

            return redirect("/venta")         

        # if request.form['btn'] == 'Ver':
        #     form.venta_id.data = request.form['venta_id']
        #     detalle_venta = DetalleVenta.query.filter_by(venta_id=form.venta_id.data).all()
        #     for detalle in detalle_venta:
        #         total += detalle.cantidad * detalle.precio_unitario
        #     ventas = Venta.query.all()

        return render_template("pages/venta/ventas.html", form=form)

    ventas = Venta.query.all()
    detalle_venta = DetalleVenta.query.all()
    for detalle in detalle_venta:
        total += detalle.cantidad * detalle.precio_unitario
    
    return render_template("pages/venta/ventas.html", form=form, ventas=ventas, total=total, detalle_venta=detalle_venta)

lista_ventas = []
@ventas.route("/venta", methods=["GET", "POST", "DELETE"])
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
    
    log.info(f"Token: {token}")
    
    idUsuario = Usuario.query.filter_by(email=token["email"]).first().id 
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

    form2 = DetalleVentaForm()

    if request.method == "POST":
        form2.process(request.form)
        tvs = tipo_venta[int(form2.tipoVenta.data)]
        gs = galletas[int(form2.galleta_id.data)]

        inventario_galletas = db.session.query(Inventario_galletas).filter_by(idGalleta=int(form2.galleta_id.data)).first().cantidad

        if request.form['btn'] == 'Añadir':
            cantidad_requerida = int(form2.cantidad.data)
            galleta_id = int(form2.galleta_id.data)

            if form2.tipoVenta.data in [1, 2]:  # Tipo de venta 1 o 2 (paquete 1kg o 700g)
                if form2.tipoVenta.data == 2:
                    cantidad_galletas = ((cantidad_requerida * 700) / gramaje[galleta_id]) 
                else:
                    cantidad_galletas = ((cantidad_requerida * 1000) / gramaje[galleta_id])
                
                if cantidad_galletas % 1 != 0:  
                    cantidad_galletas = int(cantidad_galletas)  

                if cantidad_galletas > inventario_galletas:
                    flash("No hay suficiente stock disponible", "danger")
                    return redirect("/venta")
                
                for venta in lista_ventas:
                    if venta['galleta_id'] == galleta_id:
                        if (venta['cantidad'] + cantidad_requerida) > inventario_galletas:
                            flash("No se puede agregar más de este producto, no hay suficiente stock disponible", "danger")
                            return redirect("/venta")
                        else:
                            venta['cantidad'] += cantidad_requerida
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
            else:  
                
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
                    }
                    lista_ventas.append(venta_nueva)

            total = sum(venta['cantidad'] * venta['precio_unitario'] for venta in lista_ventas)
            form.total.data = total

        if request.form['btn'] == "Vender":

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
            
        if request.form['btn'] == "Cancelar":
            lista_ventas.clear()
            return redirect("/ventas")
        
        return render_template("pages/venta/index.html", form=form, form2=form2, lista_ventas=lista_ventas, total=total, inventario_galletas=inventario_galletas)
    
    return render_template("pages/venta/index.html", form=form, form2=form2, lista_ventas=lista_ventas, total=total)

@ventas.route("/createPdf", methods=["GET", "POST","DELETE"])
@token_required
@allowed_roles(roles=["admin", "ventas"])
def create_pdf():

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
    
        subtotal_detalle = float(detalle['cantidad']) * float(detalle['precio_unitario'])  # Asegurar que la cantidad y el precio sean flotantes para la multiplicación
        total_venta += subtotal_detalle

    usuario = Usuario.query.filter_by(id=venta.idUsuario).first()

    # Renderizar el template y pasar los datos al contexto
    return render_template("pages/venta/createPdf.html", venta=venta, detalles_venta=detalles_venta, usuario=usuario, total_venta=total_venta)


