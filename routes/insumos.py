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
from forms.ProveedorForm import ProveedorForm, ProveedorEditForm
from forms.InsumoForm import InsumoForm
from forms.MateriaPrimaProveedorForm import MateriaPrimaProveedorForm
from models.proveedor import Proveedor
from models.usuario import Usuario
from models.Recetas import MateriaPrima
from models.materia_prima_proveedor import MateriaPrimaProveedor
from datetime import datetime
from db.db import db
from lib.jwt import token_required, allowed_roles, createToken, decodeToken

insumos = Blueprint("insumos", __name__, template_folder="templates")


@insumos.route("/insumos", methods=["GET"])
@token_required
@allowed_roles(roles=["admin"])
def index():
    insumos = MateriaPrima.query.all()
    mpp = MateriaPrimaProveedor.query.all()
    form = InsumoForm(request.form)
    formMPP = MateriaPrimaProveedorForm(request.form)

    all_insumos = []

    for insumo, mp in zip(insumos, mpp):
        if mp.materiaprima_id == insumo.id:
            all_insumos.append(
                {
                    "proveedor_id": mp.proveedor_id,
                    "materiaprima_id": mp.materiaprima_id,
                    "precio": mp.precio,
                    "cantidad": mp.cantidad,
                    "material": insumo.material,
                    "medida": insumo.tipo,
                    "presentacion": mp.tipo,
                }
            )

            errors = [form.errors[field][0] for field in form.errors]
            
    return render_template("pages/insumos/index.html", insumos=all_insumos, form=form, formMPP=formMPP, errors=errors)
