from flask import Blueprint, render_template, request, flash, redirect
from forms.InventarioMP import InventarioMPForm
from models.inventario_mp import InventarioMP
from db.db import db
from lib.jwt import token_required, allowed_roles, createToken, decodeToken
from datetime import datetime

inventario_mp = Blueprint("inventario_mp", __name__, template_folder="templates")

@inventario_mp.route("/inventario_mp", methods=["GET", "POST"])
@token_required
def index():
    token = request.cookies.get("token")
    
    
    return render_template("pages/inventario_mp/index.html")
