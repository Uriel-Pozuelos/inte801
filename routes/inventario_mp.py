from flask import Blueprint, render_template, request, flash, redirect
from forms.InventarioMP import InventarioMPForm
from models.inventario_mp import InventarioMP
from models.compra import Compra
from models.detalleCompra import DetalleCompra
from models.Recetas import MateriaPrima
from models.proveedor import Proveedor
from models.materia_prima_proveedor import MateriaPrimaProveedor
from models.merma_materia import MermaMateria
from models.usuario import Usuario
from db.db import db
from lib.jwt import token_required, allowed_roles, createToken, decodeToken
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from lib.d import D

log = D(debug=True)

inventario_mp = Blueprint("inventario_mp", __name__, template_folder="templates")


@inventario_mp.route("/inventario_mp", methods=["GET", "POST"])
@token_required
@allowed_roles(roles=["admin", "inventario"])
def index():
    active_token = request.cookies.get("token")
    token = decodeToken(active_token)
    email = token["email"]

    inv_mat_prima = InventarioMP.query.all()
    inv_mat_prima = [inv.serialize() for inv in inv_mat_prima]

    materias_primas = MateriaPrima.query.all()
    compras = Compra.query.all()
    all_mermas = MermaMateria.query.all()

    all_inv_mp = []
    all_merm = []
    fecha_actual = datetime.now()
    
    for merma in all_mermas:
        prov = Proveedor.query.filter_by(id=merma.id_proveedor).first()
        mat = MateriaPrima.query.filter_by(id=merma.idInventarioMaterias).first()
        
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
                

                prov = Proveedor.query.filter_by(id=prov_mpp.proveedor_id).first()
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

                all_inv_mp.append(
                    {
                        "id": inv_mp.id,
                        "nombre": material,
                        "cantidad": inv_mp.cantidad,
                        "unidad_medida": tipo,
                        "proveedor": prov.nombre_empresa,
                        "caducidad": str(fecha_caducidad).split(" ")[0],
                        "fecha_compra": inv_mp.created_at,
                        "estatus": estatus,
                        "merma": estatus_merma,
                    }
                )

    return render_template("pages/inventario_mp/index.html", materia_primas=all_inv_mp, mermas=all_merm)


@inventario_mp.route("/addmerma", methods=["GET", "POST"])
@token_required
@allowed_roles(roles=["admin", "inventario"])
def new_merma():
    active_token = request.cookies.get("token")
    token = decodeToken(active_token)
    email = token["email"]
    
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        if request.method == "POST":
            id_inv_mat = request.form.get("id_inv_mat")
            merma_tipo = request.form.get("slcMerma")
            fecha_merma = request.form.get("fecha_merma")
            cantidad_merma = request.form.get("cantidad_merma")
            justificacion_merma = request.form.get("justificacion_merma")
            id_proovedor = None
            id_produccion = None
            
            imp = InventarioMP.query.filter_by(id=id_inv_mat).first()
            
            if merma_tipo == "Proveedor":
                compra = Compra.query.filter_by(id=imp.idCompra).first()
                prov = compra.id_proveedor
                id_proovedor = prov
                
            if merma_tipo == "Produccion":
                user_production = Usuario.query.filter_by(email=email).first()
                if user_production.rol == "produccion":
                    prod = user_production.id
                    id_produccion = prod
            
            merma = MermaMateria(
                idInventarioMaterias=id_inv_mat,
                merma_tipo = merma_tipo,
                merma_fecha = fecha_merma,
                cantidad = cantidad_merma,
                created_at = current_date,
                id_produccion = id_produccion,
                id_proveedor = id_proovedor,
                justificacion = justificacion_merma
            )
            
            db.session.add(merma)
            db.session.commit()
            
            if imp:
                imp.cantidad = (int(imp.cantidad) - int(cantidad_merma))
                db.session.add(merma)
                db.session.commit()

            flash("Se ha registrado la merma correctamente", "success")
            return redirect("/inventario_mp")
    except Exception as e:
        flash("Ocurrio un error al registrar la merma", "danger")
        print(e)
        return redirect("/inventario_mp")
