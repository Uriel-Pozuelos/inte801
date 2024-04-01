from flask import Blueprint, render_template, request, flash, redirect
from forms.CompraForm import CompraForm
from forms.DetalleCompraForm import DetalleCompraForm
from models.compra import Compra
from models.detalleCompra import DetalleCompra
from datetime import datetime
from db.db import db
from lib.jwt import token_required, allowed_roles, createToken, decodeToken

compras = Blueprint("compras", __name__, template_folder="templates")

@compras.route("/compras", methods=["GET"])
def index():
    token = request.cookies.get("token")
    if not token:
        return redirect("/login")
    compras = Compra.query.all()
    return render_template("pages/purchase/index.html", compras=compras)

@compras.route("/add_purchase", methods=["GET", "POST"])
def new_purchase():
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    form = CompraForm()
    formdc = DetalleCompraForm()
    token = request.cookies.get("token")

    if not token:
        return redirect("/login")

    if request.method == "POST" and form.validate() and formdc.validate():
        id_proveedor = form.id_proveedor.data
        id_usuario = form.id_usuario.data
        created_at = fecha

        compra = Compra(
            id_proveedor=id_proveedor,
            id_usuario=id_usuario,
            created_at=created_at
        )
        
        db.session.add(compra)
        
        materia_prima = formdc.materia_prima.data
        precio_materia = formdc.precio_materia.data
        cantidad = formdc.cantidad.data
        tipo = formdc.tipo.data
        caducidad = formdc.caducidad.data
        created_at = fecha
        id_compra = compra.id
        
        dc = DetalleCompra(
            id_compra=id_compra,
            materia_prima=materia_prima,
            precio_materia=precio_materia,
            cantidad=cantidad,
            tipo=tipo,
            caducidad=caducidad,
            created_at=created_at
        )
        
        db.session.add(dc)
        db.session.commit()
                
        flash("Compra creada correctamente", "success")
        
        return redirect("/compras")
    return render_template("pages/purchase/index.html", form=form)
