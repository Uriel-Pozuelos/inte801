from flask import Blueprint, render_template, request, flash, redirect, Response
from forms.ProveedorForm import ProveedorForm, ProveedorEditForm
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

    if request.method == "POST":
        nombre_empresa = request.form.get("nombre_empresa")
        direccion_empresa = request.form.get("direccion_empresa")
        telefono_empresa = request.form.get("telefono_empresa")
        nombre_encargado = request.form.get("nombre_encargado")
        estatus = 1
        created_at = fecha
        updated_at = fecha
        deleted_at = None

        proveedor = Proveedor(
            nombre_empresa=nombre_empresa,
            direccion_empresa=direccion_empresa,
            telefono_empresa=telefono_empresa,
            nombre_encargado=nombre_encargado,
            estatus=estatus,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
        )

        db.session.add(proveedor)
        db.session.commit()
        
        flash("Proveedor creado correctamente", "success")
        
        return redirect("/proveedores")
    return render_template("pages/provider/index.html", form=form)

@proveedores.route("/edit_provider", methods=["GET", "POST"])
@token_required
def ed_provider():
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    form = ProveedorEditForm()

    if request.method == "POST" and form.validate():
        id = form.id.data
        proveedor = Proveedor.query.get(id)
        proveedor.nombre_empresa = form.nombre_empresa.data
        proveedor.direccion_empresa = form.direccion_empresa.data
        proveedor.telefono_empresa = form.telefono_empresa.data
        proveedor.nombre_atencion = form.nombre_atencion.data
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
