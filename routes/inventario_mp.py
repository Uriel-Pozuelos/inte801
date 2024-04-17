from models.inventario_mp import InventarioMP
from models.compra import Compra
from models.detalleCompra import DetalleCompra
from models.Recetas import MateriaPrima
from models.proveedor import Proveedor
from models.materia_prima_proveedor import MateriaPrimaProveedor
from models.merma_materia import MermaMateria
from models.usuario import Usuario
from models.Produccion import Produccion
from db.db import db
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from lib.d import D
from lib.security import safe
from forms.InventarioMP import InventarioMPForm
from forms.MermaMateriaForm import MermaMateriaForm
from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect)
from lib.jwt import (
    token_required,
    allowed_roles,
    createToken,
    decodeToken)

log = D(debug=True)

inventario_mp = Blueprint("inventario_mp", __name__,
                          template_folder="templates")


@inventario_mp.route("/inventario_mp", methods=["GET"])
@token_required
@allowed_roles(roles=["admin", "inventario"])
def index():
    active_token = request.cookies.get("token")
    token = decodeToken(active_token)
    email = token["email"]

    inv_mat_prima = InventarioMP.query.all()
    materias_primas = MateriaPrima.query.all()
    compras = Compra.query.all()
    all_mermas = MermaMateria.query.all()

    all_inv_mp = []
    all_merm = []
    fecha_actual = datetime.now()

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formM = MermaMateriaForm()
    formM.merma_fecha.data = datetime.now()

    for merma in all_mermas:
        prov = Proveedor.query.filter_by(id=merma.id_proveedor).first()
        mat = MateriaPrima.query.filter_by(
            id=merma.idInventarioMaterias).first()

        if merma is None or mat is None:
            continue

        all_merm.append({
            "id": merma.id,
            "idInventarioMaterias": merma.idInventarioMaterias,
            "merma_tipo": merma.merma_tipo,
            "merma_fecha": merma.merma_fecha,
            "cantidad": merma.cantidad,
            "created_at": merma.created_at,
            "id_produccion": merma.id_produccion,
            "id_proveedor": merma.id_proveedor,
            "justificacion": merma.justificacion,
            "nombre_empresa": prov.nombre_empresa,
            "material": mat.material
        })

    for inv_mp in inv_mat_prima:
        for mat in materias_primas:
            if inv_mp.id_materia_prima == mat.id:
                material = mat.material
                tipo = mat.tipo

                prov_mpp = MateriaPrimaProveedor.query.filter_by(
                    materiaprima_id=mat.id
                ).first()

                if prov_mpp is None:
                    continue

                prov = Proveedor.query.filter_by(
                    id=prov_mpp.proveedor_id).first()
                merma_inv = MermaMateria.query.filter_by(
                    idInventarioMaterias=inv_mp.id
                ).first()

                estatus_merma = ""
                fecha_caducidad = inv_mp.caducidad

                if fecha_actual > inv_mp.caducidad:
                    estatus_merma = "Caduco"
                elif fecha_actual < inv_mp.caducidad:
                    estatus_merma = "Consumible"
                elif merma_inv is not None:
                    estatus_merma = "Mermado"

                estatus = ""

                if int(inv_mp.cantidad) == 0:
                    estatus = "Agotado"
                elif int(inv_mp.cantidad) < 10 and int(inv_mp.cantidad) > 4:
                    estatus = "Por terminarse"
                elif int(inv_mp.cantidad) > 10:
                    estatus = "Disponible"

                nombre_empresa = Proveedor.query.filter_by(
                    id=prov_mpp.proveedor_id).first().nombre_empresa

                all_inv_mp.append(
                    {
                        "id": inv_mp.id,
                        "nombre": material,
                        "cantidad": inv_mp.cantidad,
                        "unidad_medida": tipo,
                        "proveedor": nombre_empresa,
                        "caducidad": str(fecha_caducidad).split(" ")[0],
                        "fecha_compra": inv_mp.created_at,
                        "estatus": estatus,
                        "merma": estatus_merma,
                    }
                )

    return render_template("pages/inventario_mp/index.html", materia_primas=all_inv_mp, mermas=all_merm, formM=formM)


@inventario_mp.route("/addmerma", methods=["POST"])
@token_required
@allowed_roles(roles=["admin", "inventario"])
def new_merma():
    active_token = request.cookies.get("token")
    token = decodeToken(active_token)
    email = token["email"]

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    form = MermaMateriaForm(request.form)

    try:
        id_inv_mat = request.form.get("id")
        merma_tipo = form.merma_tipo.data
        fecha_merma = form.merma_fecha.data
        cantidad_merma = form.cantidad.data
        justificacion_merma = form.justificacion.data

        imp = InventarioMP.query.filter_by(
            id=id_inv_mat, estatus=1).first()

        if imp is not None:
            if int(imp.cantidad) - int(cantidad_merma) > 0:

                compra = Compra.query.filter_by(id=imp.idCompra).first()
                proveedor = compra.id_proveedor

                merma = MermaMateria(
                    idInventarioMaterias=imp.id,
                    merma_tipo=safe(merma_tipo),
                    merma_fecha=safe(fecha_merma),
                    cantidad=safe(cantidad_merma),
                    justificacion=safe(justificacion_merma),
                    created_at=current_date,
                    id_produccion=None,
                    id_proveedor=int(proveedor),
                )

                db.session.add(merma)

                imp.cantidad = (int(imp.cantidad) - int(cantidad_merma))

                db.session.commit()

                flash("Se ha registrado la merma correctamente", "success")
            else:
                flash(
                    "La cantidad a mermar sobre pasa la cantidad total en inventario", "error")
        return redirect("/inventario_mp")
    except Exception as e:
        flash("Ocurrio un error al registrar la merma", "danger")
        db.session.rollback()
        log.error(e)
        return redirect("/inventario_mp")
