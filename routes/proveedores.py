from flask import Blueprint, render_template, request, flash, redirect, Response
from forms.ProveedorForm import ProveedorForm, ProveedorEditForm
from models.proveedor import Proveedor
from models.usuario import Usuario
from models.materia_prima_proveedor import MateriaPrimaProveedor
from datetime import datetime
from db.db import db
from lib.jwt import token_required, allowed_roles, createToken, decodeToken

proveedores = Blueprint("proveedores", __name__, template_folder="templates")


@proveedores.route("/proveedores", methods=["GET", "POST"])
@token_required
def index():
    active_token = request.cookies.get('token')
    token = decodeToken(active_token)
    email = token['email']

    form = ProveedorForm()
    formE = ProveedorEditForm()
    proveedores = Proveedor.query.filter_by(estatus=1).all()
    current_user = Usuario.query.filter_by(email=email).first()

    if request.method == 'POST':
        pass

    return render_template("pages/provider/index.html", proveedores=proveedores, form=form, current_user=current_user.id)


@proveedores.route("/add_provider", methods=["GET", "POST"])
@token_required
def new_provider():
    try:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form = ProveedorForm()

        active_token = request.cookies.get('token')
        token = decodeToken(active_token)
        email = token['email']

        if request.method == "POST":
            current_user = Usuario.query.filter_by(email=email).first()
            nombre_empresa = request.form.get("nombre_empresa")
            direccion_empresa = request.form.get("direccion_empresa")
            telefono_empresa = request.form.get("telefono_empresa")
            nombre_encargado = request.form.get("nombre_encargado")
            estatus = 1
            created_at = fecha
            updated_at = fecha
            deleted_at = None
            id_usuario = current_user.id

            proveedor = Proveedor(
                nombre_empresa=nombre_empresa,
                direccion_empresa=direccion_empresa,
                telefono_empresa=telefono_empresa,
                nombre_encargado=nombre_encargado,
                estatus=estatus,
                created_at=created_at,
                updated_at=updated_at,
                deleted_at=deleted_at,
                id_usuario=id_usuario
            )

            # db.session.add(proveedor)

            # Obtener los valores de las filas dinámicas
            productos = request.form.getlist("producto[]")
            precios = request.form.getlist("precio[]")

            for producto, precio in zip(productos, precios):
                mpp = MateriaPrimaProveedor(
                    proveedor_id = proveedor.id
                )

            # db.session.commit()

            flash("Proveedor creado correctamente", "success")

            return redirect("/proveedores")
        return render_template("pages/provider/index.html", form=form)
    except Exception as e:
        flash(str(e), "error")
        return redirect("/proveedores")


@proveedores.route("/edit_provider", methods=["GET", "POST"])
@token_required
def ed_provider():
    active_token = request.cookies.get('token')
    token = decodeToken(active_token)
    email = token['email']

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    form = ProveedorEditForm()
    current_user = Usuario.query.filter_by(email=email).first()

    if request.method == "POST":
        id = request.form.get("id")
        proveedor = Proveedor.query.get(id)
        proveedor.nombre_empresa = request.form.get("nombre_empresa_edit")
        proveedor.direccion_empresa = request.form.get(
            "direccion_empresa_edit")
        proveedor.telefono_empresa = request.form.get("telefono_empresa_edit")
        proveedor.nombre_encargado = request.form.get("nombre_encargado_edit")
        proveedor.updated_at = fecha
        proveedor.id_usuario = current_user.id

        db.session.commit()

        flash("Proveedor actualizado correctamente", "success")

        return redirect("/proveedores")
    return render_template("pages/provider/index.html", form=form)


@proveedores.route("/delete_provider", methods=["GET", "POST"])
def del_provider():
    active_token = request.cookies.get('token')
    token = decodeToken(active_token)
    email = token['email']

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    form = ProveedorForm()
    current_user = Usuario.query.filter_by(email=email).first()

    if request.method == "POST":
        id = request.form.get("id_del")
        proveedor = Proveedor.query.get(id)
        proveedor.estatus = 0
        proveedor.deleted_at = fecha
        proveedor.id_usuario = current_user.id

        db.session.commit()

        flash("Proveedor eliminado correctamente", "success")

        return redirect("/proveedores")
    return render_template("pages/provider/index.html", form=form)
