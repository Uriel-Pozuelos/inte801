from flask import Blueprint, render_template, request, flash, redirect
from forms.CompraForm import CompraForm
from forms.DetalleCompraForm import DetalleCompraForm
from models.compra import Compra
from models.detalleCompra import DetalleCompra
from datetime import datetime
from db.db import db
from lib.jwt import token_required, allowed_roles, createToken, decodeToken

compras = Blueprint("compras", __name__, template_folder="templates")

@compras.route("/compras", methods=["GET", "POST"])
@token_required
def index():
    token = request.cookies.get("token")
    
    return render_template("pages/compras/index.html")

