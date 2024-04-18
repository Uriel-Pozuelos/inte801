from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    Response,
    jsonify,
    g,
)
from models.proveedor import Proveedor
from models.usuario import Usuario
from models.Recetas import MateriaPrima
from models.materia_prima_proveedor import MateriaPrimaProveedor
from forms.ProveedorForm import ProveedorForm, ProveedorEditForm, ProveedorDelForm
from datetime import datetime
from db.db import db
from lib.jwt import token_required, allowed_roles, createToken, decodeToken
from lib.security import safe

proveedores = Blueprint("proveedores", __name__, template_folder="templates")


@proveedores.route("/proveedores", methods=["GET", "POST"])
@token_required
@allowed_roles(roles=["admin", "compras"])
def index():
    active_token = request.cookies.get("token")
    token = decodeToken(active_token)
    email = token["email"]

    form = ProveedorForm(request.form)
    formEP = ProveedorEditForm(request.form)
    formDP = ProveedorDelForm(request.form)
    proveedores = Proveedor.query.filter_by(estatus=1).all()
    provs = []

    for prov in proveedores:
        provs.append(
            {
                "id": prov.id,
                "nombre_empresa": prov.nombre_empresa,
                "direccion_empresa": prov.direccion_empresa,
                "telefono_empresa": prov.telefono_empresa,
                "nombre_encargado": prov.nombre_encargado,
                "estatus": prov.estatus,
                "created_at": prov.created_at,
                "updated_at": prov.updated_at,
                "deleted_at": prov.deleted_at,
                "id_usuario": prov.id_usuario,
            }
        )

    return render_template(
        "pages/provider/index.html",
        proveedores=provs,
        form=form,
        formEP=formEP,
        formDP=formDP,
    )


@proveedores.route("/add_provider", methods=["POST"])
@token_required
@allowed_roles(roles=["admin", "compras"])
def new_provider():
    try:
        form = ProveedorForm(request.form)
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        active_token = request.cookies.get("token")
        token = decodeToken(active_token)
        email = token["email"]
        current_user = Usuario.query.filter_by(email=email).first()

        proveedor = Proveedor(
            nombre_empresa=safe(form.nombre_empresa.data),
            direccion_empresa=safe(form.direccion_empresa.data),
            telefono_empresa=safe(form.telefono_empresa.data),
            nombre_encargado=safe(form.nombre_encargado.data),
            estatus=1,
            created_at=fecha,
            updated_at=fecha,
            id_usuario=current_user.id,
        )

        db.session.add(proveedor)
        db.session.commit()

        flash("Proveedor creado correctamente", "success")
        return redirect("/proveedores")
    except Exception as e:
        db.session.rollback()
        print(e)
        flash("Ocurrio un error al crear el proveedor", "error")
        return redirect("/proveedores")


@proveedores.route("/edit_provider", methods=["POST"])
@token_required
@allowed_roles(roles=["admin", "compras"])
def ed_provider():
    active_token = request.cookies.get("token")
    token = decodeToken(active_token)
    email = token["email"]

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_user = Usuario.query.filter_by(email=email).first()

    formEP = ProveedorEditForm(request.form)
    empresa = safe(formEP.nombre_empresa_edit.data)
    direccion = safe(formEP.direccion_empresa_edit.data)
    tel = safe(formEP.telefono_empresa_edit.data)
    encargado = safe(formEP.nombre_encargado_edit.data)

    try:
        id = request.form.get("id")
        proveedor = Proveedor.query.get(id)

        proveedor.nombre_empresa = empresa if empresa is not None else proveedor.nombre_empresa
        proveedor.direccion_empresa = direccion if direccion is not None else proveedor.direccion_empresa
        proveedor.telefono_empresa = tel if tel is not None and len(
            tel) == 10 else proveedor.telefono_empresa
        proveedor.nombre_encargado = encargado if encargado is not None else proveedor.nombre_encargado
        proveedor.id_usuario = current_user.id

        db.session.commit()

        flash("Proveedor actualizado correctamente", "success")
        return redirect("/proveedores")
    except Exception as e:
        db.session.rollback()
        flash("Ocurrio un error al actualizar los datos", "error")
        return redirect("/proveedores")


@proveedores.route("/delete_provider", methods=["GET", "POST"])
@token_required
@allowed_roles(roles=["admin", "compras"])
def del_provider():
    active_token = request.cookies.get("token")
    token = decodeToken(active_token)
    email = token["email"]

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_user = Usuario.query.filter_by(email=email).first()
    formDP = ProveedorDelForm(request.form)

    try:
        id = request.form.get("id_del")
        proveedor = Proveedor.query.get(id)

        proveedor.estatus = 0
        proveedor.deleted_at = fecha
        proveedor.id_usuario = current_user.id

        db.session.commit()

        flash("Proveedor eliminado correctamente", "success")
        return redirect("/proveedores")
    except Exception as e:
        db.session.rollback()
        flash("Ocurrio un error al eliminar el proveedor", "error")
        return redirect("/proveedores")
