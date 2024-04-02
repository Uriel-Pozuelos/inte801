from flask import Blueprint, request, render_template, flash
from models.usuario import Usuario,db
from lib.jwt import allowed_roles, token_required,decodeToken
from forms.Usuario import UsuarioForm
from lib.d import D

log = D(debug=True)

usuario = Blueprint('usuario', __name__)

def get_usuarios():
    usuarios = Usuario.query.all()
    usuarios = [usuario.serialize() for usuario in usuarios]
    return usuarios

def delete_usuario_by_id(id):
    usuario = Usuario.query.filter_by(id=id).first()
    db.session.delete(usuario)
    db.session.commit()


def update_usuario_by_id(id,form):
    usuario = Usuario.query.filter_by(id=id).first()
    usuario.nombre = form.nombre.data
    usuario.apellido = form.apellido.data
    usuario.email = form.email.data
    usuario.rol = form.rol.data
    db.session.commit()

def add_usuario(form):
    usuario = Usuario(nombre=form.nombre.data, apellido=form.apellido.data, email=form.email.data, password=form.password.data, rol=form.rol.data,estado='activo')
    db.session.add(usuario)
    db.session.commit()






@usuario.route('/usuario', methods=['GET', 'POST'])
@token_required
def index():
    log.warning(request.form)
    form = UsuarioForm(request.form)
    if request.method == 'POST':
        if 'remove' in request.form:
            delete_usuario_by_id(form.id.data)
            flash('Usuario eliminado correctamente')
        elif 'edit' in request.form:
            
            if not form.validate():

                log.error('Error al editar el usuario')
                flash('Error al editar el usuario', 'danger')


                errors = [form.errors[field][0] for field in form.errors]
                log.info(errors)
            
                return render_template('pages/usuario/index.html', form=form, usuarios=get_usuarios(), showModal='true', Mode='edit',errors=errors)

            token = decodeToken(request.cookies.get('token'))
            if token['email'] == form.email.data:
                flash('No puedes editar tu propio usuario')
                return render_template('pages/usuario/index.html', form=form, usuarios=get_usuarios(), showModal='false', Mode='edit', errors=None)
            update_usuario_by_id(form.id.data, form)
            flash('Usuario editado correctamente')
        elif 'add' in request.form:
            if not form.validate():
                form.errors.pop('password')

                log.error('Error al agregar el usuario')

                flash('Error al agregar el usuario', 'danger')
                errors = [form.errors[field][0] for field in form.errors]
                log.info(errors)
                return render_template('pages/usuario/index.html', form=form, usuarios=get_usuarios(), showModal='true', Mode='add', errors=errors)
            add_usuario(form)
            flash('Usuario agregado correctamente')
        else:
            flash('Error al procesar la solicitud')
            

    return render_template('pages/usuario/index.html', form=form, usuarios=get_usuarios(), showModal='false', Mode='edit', errors=None)
