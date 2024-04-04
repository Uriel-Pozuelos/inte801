from flask import Blueprint, render_template, request, flash, redirect
from forms.ProveedorForm import ProveedorForm
from models.proveedor import Proveedor
from datetime import datetime
from db.db import db
from lib.jwt import token_required, allowed_roles, createToken, decodeToken

proveedores = Blueprint("proveedores", __name__, template_folder="templates")

@proveedores.route("/proveedores", methods=["GET", "POST"])
@token_required
def index():
    form = ProveedorForm()
    proveedores = Proveedor.query.all()
    
    if request.method == 'POST':
        pass
    
    return render_template("pages/provider/index.html", proveedores=proveedores, form=form)

@proveedores.route("/add_provider", methods=["GET", "POST"])
@token_required
def new_provider():
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    form = ProveedorForm()

    if request.method == "POST" and form.validate():
        nombre_empresa = form.str_nombre_empresa.data
        direccion_empresa = form.str_direccion.data
        telefono_empresa = form.str_telefono.data
        nombre_atencion = form.str_atencion.data
        productos = form.str_productos.data
        estatus = 1
        created_at = fecha
        updated_at = fecha
        deleted_at = None

        proveedor = Proveedor(
            nombre_empresa=nombre_empresa,
            direccion_empresa=direccion_empresa,
            telefono_empresa=telefono_empresa,
            nombre_atencion=nombre_atencion,
            productos=productos,
            estatus=estatus,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
        )
        print(proveedor)

        # db.session.add(proveedor)
        # db.session.commit()
        
        # flash("Proveedor creado correctamente", "success")
        
        # return redirect("/proveedores")
    return render_template("pages/provider/index.html", form=form)

@proveedores.route("/edit_provider", methods=["GET", "POST"])
@token_required
def ed_provider():
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    form = ProveedorForm()

    if request.method == "POST" and form.validate():
        id = form.id.data
        proveedor = Proveedor.query.get(id)
        proveedor.nombre_empresa = form.nombre_empresa.data
        proveedor.direccion_empresa = form.direccion_empresa.data
        proveedor.telefono_empresa = form.telefono_empresa.data
        proveedor.nombre_atencion = form.nombre_atencion.data
        proveedor.productos = form.productos.data
        proveedor.estatus = form.estatus.data
        proveedor.updated_at = fecha

        db.session.commit()
        
        flash("Proveedor actualizado correctamente", "success")
        
        return redirect("/proveedores")
    return render_template("pages/provider/index.html", form=form)

@proveedores.route("/delete_provider", methods=["GET", "POST"])
def del_provider():
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    form = ProveedorForm()
    
    if request.method == "POST" and form.validate():
        id = form.id.data
        proveedor = Proveedor.query.get(id)
        proveedor.estatus = "Inactivo"
        proveedor.deleted_at = fecha

        db.session.commit()
        
        flash("Proveedor eliminado correctamente", "success")
        
        return redirect("/proveedores")
    return render_template("pages/provider/index.html", form=form)
