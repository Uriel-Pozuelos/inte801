from flask import Blueprint, render_template, request, flash, redirect
from forms.VentaForm import Venta
from models.venta import Venta
# from models.Galletas import Galletas
from models.detalleVenta import DetalleVenta
from datetime import datetime
from db.db import db
from lib.jwt import token_required, allowed_roles, createToken, decodeToken

ventas = Blueprint("ventas", __name__, template_folder="templates")

@ventas.route("/ventas", methods=["GET"])
def index():
    token = request.cookies.get("token")
    if not token:
        return redirect("/login")
    ventas = Venta.query.all()
    return render_template("pages/venta/ventas.html", ventas=ventas)

@ventas.route("/add_venta", methods=["GET", "POST"])
def new_venta():
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    form = Venta()
    token = request.cookies.get("token")
    
    if not token:
        return redirect("/login")
    
    return render_template("pages/venta/index.html", form=form)
