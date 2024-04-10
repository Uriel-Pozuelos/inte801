from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    Response,
    jsonify,
    g
)
from forms.ProveedorForm import ProveedorForm, ProveedorEditForm
from models.proveedor import Proveedor
from models.usuario import Usuario
from models.Recetas import MateriaPrima
from models.materia_prima_proveedor import MateriaPrimaProveedor
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

    form = ProveedorForm()
    formE = ProveedorEditForm()

    proveedores = Proveedor.query.filter_by(estatus=1).all()
    current_user = Usuario.query.filter_by(email=email).first()
    mat_prim_prov = MateriaPrimaProveedor.query.all()
    materiap = MateriaPrima.query.all()

    tbl_prov = []
    mats_list = []

    for prov in proveedores:
        for mat in mat_prim_prov:
            if mat.proveedor_id == prov.id:
                for mp in materiap:
                    if mp.id == mat.materiaprima_id:
                        mats_list.append(
                            {
                                "id": mat.materiaprima_id,
                                "material": mp.material,
                                "precio": mat.precio,
                                "cantidad": mat.cantidad,
                                "tipo": mat.tipo,
                                "proveedor_id": mat.proveedor_id,
                                "material_tipo": mp.tipo,
                            }
                        )
        tbl_prov.append(
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
                "mats_list": mats_list,
            }
        )

    if request.method == "POST":
        pass

    return render_template(
        "pages/provider/index.html",
        proveedores=proveedores,
        form=form,
        current_user=current_user.id,
        tbl_prov=tbl_prov,
        mats_list=mats_list
    )


@proveedores.route("/add_provider", methods=["GET", "POST"])
@token_required
@allowed_roles(roles=["admin", "compras"])
def new_provider():
    try:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form = ProveedorForm()

        active_token = request.cookies.get("token")
        token = decodeToken(active_token)
        email = token["email"]

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
                nombre_empresa=str(nombre_empresa),
                direccion_empresa=str(direccion_empresa),
                telefono_empresa=str(telefono_empresa),
                nombre_encargado=str(nombre_encargado),
                estatus=estatus,
                created_at=created_at,
                updated_at=updated_at,
                deleted_at=deleted_at,
                id_usuario=id_usuario,
            )

            db.session.add(proveedor)
            db.session.commit()

            productos = request.form.getlist("producto[]")
            precios = request.form.getlist("precio[]")
            cantidad = request.form.getlist("cantidad[]")
            presentacion = request.form.getlist("presentacion[]")
            medida =  request.form.getlist("medida[]")

            print(productos)
            print(precios)
            print(cantidad)
            print(presentacion)
            print(medida)

            for producto, precio, cant, pres, med in zip(productos, precios, cantidad, presentacion, medida):
                mp = MateriaPrima.query.filter_by(
                    material=producto.lower()).first()

                
                mp = MateriaPrima(
                        material=str(producto),
                        tipo=str(med),
                        estatus=1,
                        created_at=fecha,
                        updated_at=fecha,
                        deleted_at=None,
                    )

                db.session.add(mp)
                db.session.commit()

                mat_prim_prov = MateriaPrimaProveedor(
                    materiaprima_id=mp.id,
                    proveedor_id=proveedor.id,
                    precio=float(precio),
                    cantidad=cant,
                    tipo=pres,
                    created_at=fecha,
                )

                db.session.add(mat_prim_prov)
                db.session.commit()

            flash("Proveedor creado correctamente", "success")

            return redirect("/proveedores")
        return render_template("pages/provider/index.html", form=form)
    except Exception as e:
        db.session.rollback()
        flash(str(e), "error")
        return str(e)


@proveedores.route("/edit_provider", methods=["GET", "POST"])
@token_required
@allowed_roles(roles=["admin", "compras"])
def ed_provider():
    active_token = request.cookies.get("token")
    token = decodeToken(active_token)
    email = token["email"]

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    form = ProveedorEditForm()
    current_user = Usuario.query.filter_by(email=email).first()

    try:
        if request.method == "POST":
            id = request.form.get("id")
            proveedor = Proveedor.query.get(id)
            proveedor.nombre_empresa = request.form.get("nombre_empresa_edit")
            proveedor.direccion_empresa = request.form.get(
                "direccion_empresa_edit")
            proveedor.telefono_empresa = request.form.get(
                "telefono_empresa_edit")
            proveedor.nombre_encargado = request.form.get(
                "nombre_encargado_edit")
            proveedor.updated_at = fecha
            proveedor.id_usuario = current_user.id

            # productos_list = request.form.getlist("producto_edit[]")
            # precio_list = request.form.getlist("precio_edit[]")
            # cantidad_list = request.form.getlist("cantidad_edit[]")
            # tipo_list = request.form.getlist("tipo_edit[]")
            # id_list = request.form.getlist("material_id[]")

            # if len(tipo_list) == 0:
            #     for idl, producto, precio, cant in zip(
            #         id_list, productos_list, precio_list, cantidad_list
            #     ):
            #         materia_prima = MateriaPrima.query.get(idl)
            #         mpp = MateriaPrimaProveedor.query.filter_by(
            #             materiaprima_id=materia_prima.id, proveedor_id=proveedor.id
            #         ).first()

            #         mpp.precio = precio
            #         mpp.cantidad = cant

            #         materia_prima.material = producto

            # else:
            #     for idl, producto, precio, cant, tip in zip(
            #         id_list, productos_list, precio_list, cantidad_list, tipo_list
            #     ):
            #         materia_prima = MateriaPrima.query.get(idl)
            #         mpp = MateriaPrimaProveedor.query.filter_by(
            #             materiaprima_id=materia_prima.id, proveedor_id=proveedor.id
            #         ).first()

            #         presentacion = tip.split("-")[0]
            #         tipom = tip.split("-")[1]

            #         mpp.precio = precio
            #         mpp.cantidad = cant
            #         mpp.tipo = presentacion

            #         materia_prima.material = producto
            #         materia_prima.tipo = tipom

            db.session.commit()

            flash("Proveedor actualizado correctamente", "success")

            return redirect("/proveedores")
        return redirect("/proveedores")
    except Exception as e:
        db.session.rollback()
        print(str(e))
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
            precios_list = request.form.getlist("precio_edit[]")
            cantidad_list = request.form.getlist("cantidad_edit[]")
            tipos_list = request.form.getlist("tipo_edit[]")
            id_list = request.form.getlist("matids[]")
            prov_id = request.form.get("providerId")

            presentacion = ""
            medida = ""

            proveedor = Proveedor.query.filter_by(id=int(prov_id)).first()
            mpp = MateriaPrimaProveedor.query.all()

            for product, precio, cantidad, tipo, mid in zip(productos_list, precios_list, cantidad_list, tipos_list, id_list):
                if tipo:
                    presentacion = tipo.split("-")[0]
                    medida = tipo.split("-")[1]

                    for mp in mpp:
                        if mp.materiaprima_id == int(mid) and mp.proveedor_id == int(proveedor.id):
                            materia = MateriaPrima.query.filter_by(
                                id=mp.materiaprima_id).first()
                            materia.material = product
                            materia.tipo = medida

                            mp.precio = precio
                            mp.cantidad = cantidad
                            mp.tipo = presentacion

                            db.session.commit()
                else:
                    for mp in mpp:
                        if mp.materiaprima_id == int(mid) and mp.proveedor_id == int(proveedor.id):
                            materia = MateriaPrima.query.filter_by(
                                id=mp.materiaprima_id).first()
                            materia.material = product

                            mp.precio = precio
                            mp.cantidad = cantidad

                            db.session.commit()

            flash("Materiales actualizados correctamente", "success")
            return redirect("/proveedores")
        return redirect("/proveedores")
    except Exception as ex:
        print(str(ex))
        flash("Se produjo un error al actualizar las materias primas", "error")
        return str(ex)
