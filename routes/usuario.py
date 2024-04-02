from flask import Blueprint, request, render_template
from models.usuario import Usuario,db
from lib.jwt import allowed_roles, token_required
from forms.Usuario import UsuarioForm

usuario = Blueprint('usuario', __name__)

def get_usuarios():
    usuarios = Usuario.query.all()
    usuarios = [usuario.serialize() for usuario in usuarios]
    return usuarios


@usuario.route('/usuario', methods=['GET', 'POST'])
@token_required
def index():
    form = UsuarioForm()
    usuarios = get_usuarios()
    if request.method == 'POST':
        pass
    return render_template('pages/usuario/index.html', form=form, usuarios=usuarios)