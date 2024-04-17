from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    jsonify,
    Response,
)
from forms.CompraForm import CompraForm
from forms.DetalleCompraForm import DetalleCompraForm
from models.compra import Compra
from models.proveedor import Proveedor
from models.detalleCompra import DetalleCompra
from models.Recetas import MateriaPrima
from models.usuario import Usuario
from models.materia_prima_proveedor import MateriaPrimaProveedor
from models.inventario_mp import InventarioMP
from datetime import datetime
from db.db import db
from lib.jwt import token_required, allowed_roles, createToken, decodeToken
from lib.security import safe

compras = Blueprint("compras", __name__, template_folder="templates")


@compras.route("/compras", methods=["GET", "POST"])
@token_required
@allowed_roles(roles=["admin", "inventario"])
def index():
    active_token = request.cookies.get("token")
    token = decodeToken(active_token)
    email = token["email"]

    form = CompraForm()
    formDC = DetalleCompraForm(request.form)

    compras = Compra.query.all()
    det_com = DetalleCompra.query.all()
    proveedores = Proveedor.query.all()
    materias = MateriaPrima.query.all()
    mpp = MateriaPrimaProveedor.query.all()
    usuarios = Usuario.query.all()

    form.id_proveedor.choices = [
        (prov.id, prov.nombre_empresa)
        for prov in Proveedor.query.filter_by(estatus=1).all()
    ]

    compras_generales = []
    materias_primas_by_proveedor = []
    provs = []

    options = []
    mats = []

    for mp in mpp:
        for prov in proveedores:
            if mp.proveedor_id == prov.id:
                mat = MateriaPrima.query.filter_by(id=mp.materiaprima_id).first()
                mats.append(
                    {
                        "id": mat.id,
                        "material": mat.material,
                        "presentacion": mp.tipo,
                        "precio": mp.precio,
                        "cantidad": mp.cantidad,
                        "medida": mp.tipo,
                    }
                )

                options.append(
                    {
                        "id_proveedor": prov.id,
                        "mats": mats,
                    }
                )

    for compra in compras:
        for det in det_com:
            if compra.id == det.id_compra:
                for prov in proveedores:
                    if compra.id_proveedor == prov.id:
                        for mat in materias:
                            if det.id_materia == mat.id:
                                for user in usuarios:
                                    if compra.id_usuario == user.id:
                                        compras_generales.append(
                                            {
                                                "id": compra.id,
                                                "proveedor": prov.nombre_empresa,
                                                "usuario": user.nombre,
                                                "material": mat.material,
                                                "cantidad": det.cantidad,
                                                "precio": det.precio_materia,
                                                "tipo": det.tipo,
                                                "fecha": compra.created_at,
                                            }
                                        )

    return render_template(
        "pages/compras/index.html",
        compras=compras_generales,
        cont=len(compras_generales),
        proveedores_list=proveedores,
        materias_list=materias_primas_by_proveedor,
        usuarios_list=usuarios,
        options=options,
        form=form,
    )


@compras.route("/compras/materia_prima", methods=["GET", "POST"])
@token_required
@allowed_roles(roles=["admin", "inventario"])
def get_mat():
    prov_id = request.json["proveedor_id"]

    mpp = MateriaPrimaProveedor.query.all()
    materias = MateriaPrima.query.all()
    materias_primas_by_proveedor = []

    for mp in mpp:
        if int(prov_id) == mp.proveedor_id:
            for mat in materias:
                if mp.materiaprima_id == mat.id:
                    materias_primas_by_proveedor.append(
                        {
                            "id": int(mat.id),
                            "material": str(mat.material),
                            "presentacion": str(mp.tipo),
                        }
                    )
    print(materias_primas_by_proveedor)
    return jsonify(materias_primas_by_proveedor)


@compras.route("/purchase", methods=["POST"])
@token_required
@allowed_roles(roles=["admin", "inventario"])
def purchase():
    active_token = request.cookies.get("token")
    token = decodeToken(active_token)
    email = token["email"]

    current_user = Usuario.query.filter_by(email=email).first()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        prov_id = request.form.get("slcProvider")

        compra = Compra(
            id_proveedor=prov_id,
            id_usuario=current_user.id,
            created_at=created_at,
        )

        db.session.add(compra)
        db.session.commit()

        mat_list = request.form.getlist("slcMateriaPrima[]")
        cantidad_list = request.form.getlist("txtCantidad[]")
        precio_list = request.form.getlist("txtPrecio[]")
        caduci_list = request.form.getlist("txtCaducidad[]")

        for ml, cl, pl, cad in zip(mat_list, cantidad_list, precio_list, caduci_list):
            presentacion = ml.split("-")[1]
            mat_id = ml.split("-")[0]

            det_compra = DetalleCompra(
                id_materia=safe(mat_id),
                precio_materia=safe(pl),
                cantidad=safe(cl),
                tipo=safe(presentacion),
                caducidad=safe(cad),
                id_compra=compra.id,
                created_at=created_at,
            )

            db.session.add(det_compra)
            db.session.commit()

            tipo = presentacion.split("_")[0]
            peso = presentacion.split("_")[1]
            medida = None

            if peso.find("kg") != -1:
                peso = peso.replace("kg", "")
                medida = (int(peso) * 1000) * int(cl)
            elif peso.find("ml") != -1:
                peso = peso.replace("ml", "")
                medida = (int(peso) * int(cl))
            elif peso.find("g") != -1:
                peso = peso.replace("g", "")
                medida = (int(peso) * int(cl))
            elif peso.find("lt") != -1:
                peso = int(peso) * 1000
                medida = (int(peso) * int(cl))

            inv_mpp = InventarioMP(
                id_materia_prima=mat_id,
                cantidad=medida,
                idCompra=compra.id,
                caducidad=cad,
                estatus=1,
                created_at=created_at,
            )

            db.session.add(inv_mpp)
            db.session.commit()

        flash("Compra realizada correctamente", "success")
        return redirect("/compras")
    except Exception as ex:
        print(ex)
        db.session.rollback()
        flash("Error al realizar la compra", "danger")
        return redirect("/compras")


def cleanNumber(number):
    return number.replace("e", "")
