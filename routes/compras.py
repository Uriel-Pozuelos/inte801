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

compras = Blueprint("compras", __name__, template_folder="templates")


@compras.route("/compras", methods=["GET", "POST"])
@token_required
@allowed_roles(roles=["admin", "inventario"])
def index():
    active_token = request.cookies.get("token")
    token = decodeToken(active_token)
    email = token["email"]

    compras = Compra.query.all()
    det_com = DetalleCompra.query.all()
    proveedores = Proveedor.query.all()
    materias = MateriaPrima.query.all()
    mpp = MateriaPrimaProveedor.query.all()
    usuarios = Usuario.query.all()

    compras_generales = []
    materias_primas_by_proveedor = []
    provs = []

    

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


@compras.route("/compras/purchase", methods=["GET", "POST"])
@token_required
@allowed_roles(roles=["admin", "inventario"])
def purchase():
    active_token = request.cookies.get("token")
    token = decodeToken(active_token)
    email = token["email"]

    try:
        if request.method == "POST":
            prov_id = request.form.get("slcProvider")
            current_user = Usuario.query.filter_by(email=email).first()
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

            for ml in mat_list:
                presentacion = ml.split(" - ")[1]
                mat_id = ml.split(" - ")[0]
                for pl in precio_list:
                    for cl in caduci_list:
                        for cant in cantidad_list:
                            det_compra = DetalleCompra(
                                id_materia=mat_id,
                                precio_materia=pl,
                                cantidad=cant,
                                tipo=presentacion,
                                caducidad=cl,
                                id_compra=compra.id,
                                created_at=created_at,
                            )

                            db.session.add(det_compra)
                            db.session.commit()
                            
                            cant_mpp = MateriaPrimaProveedor.query.filter_by(materiaprima_id=mat_id).first()
                            
                            inv_mat_prima = InventarioMP(
                                id_materia_prima = mat_id,
                                cantidad = (int(cant_mpp.cantidad) * int(cant)),
                                idCompra = compra.id,
                                caducidad = cl,
                                estatus = 1,
                                created_at = created_at
                            )
                            
                            db.session.add(inv_mat_prima)
                            db.session.commit()

            flash("Compra realizada con éxito", "success")

            return redirect("/compras")
    except Exception as ex:
        print(ex)
        flash("Error al realizar la compra", "danger")
        return redirect("/compras")


def cleanNumber(number):
    return number.replace('e', '')