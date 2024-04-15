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
            nombre_empresa=form.nombre_empresa.data,
            direccion_empresa=form.direccion_empresa.data,
            telefono_empresa=form.telefono_empresa.data,
            nombre_encargado=form.nombre_encargado.data,
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
    empresa = formEP.nombre_empresa_edit.data
    direccion = formEP.direccion_empresa_edit.data
    tel = formEP.telefono_empresa_edit.data
    encargado = formEP.nombre_encargado_edit.data

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


@proveedores.route("/get_materials", methods=["GET", "POST"])
@token_required
@allowed_roles(roles=["admin", "compras"])
def get_mats():
    pov_id = request.json["proveedor_id"]
    mats_list = []

    mats = MateriaPrimaProveedor.query.filter_by(proveedor_id=pov_id).all()
    for mat in mats:
        material = MateriaPrima.query.filter_by(id=mat.materiaprima_id).first()

        mats_list.append(
            {
                "id": mat.materiaprima_id,
                "material": material.material,
                "precio": mat.precio,
                "cantidad": mat.cantidad,
                "tipo": mat.tipo,
            }
        )

    return jsonify(mats_list)


@proveedores.route("/edit_mats", methods=["GET", "POST"])
@token_required
@allowed_roles(roles=["admin"])
def ed_mats():
    try:
        if request.method == "POST":
            productos_list = request.form.getlist("producto_edit[]")
            precio_list = request.form.getlist("precio_edit[]")
            cantidad_list = request.form.getlist("cantidad_edit[]")
            presentacion_list = request.form.getlist("presentacion_edit[]")
            medida_list = request.form.getlist("medida_edit[]")
            id_list = request.form.getlist("material_id[]")
            prov_id = request.form.get("providerId")
            proveedor = Proveedor.query.get(prov_id)

            for idl, producto, precio, cant, pres, med in zip(
                id_list,
                productos_list,
                precio_list,
                cantidad_list,
                presentacion_list,
                medida_list,
            ):
                materia_prima = MateriaPrima.query.get(idl)
                mpp = MateriaPrimaProveedor.query.filter_by(
                    materiaprima_id=materia_prima.id, proveedor_id=proveedor.id
                ).first()

                mpp.precio = precio
                mpp.cantidad = cant
                mpp.tipo = pres

                materia_prima.material = producto
                materia_prima.tipo = med

                db.session.commit()

            flash("Materiales actualizados correctamente", "success")
            return redirect("/proveedores")
        return redirect("/proveedores")
    except Exception as ex:
        print(str(ex))
        flash("Se produjo un error al actualizar las materias primas", "error")
        return str(ex)
