from flask import Blueprint, request, render_template, flash
from models.usuario import Usuario,db
from lib.jwt import allowed_roles, token_required,decodeToken,hash_password
from forms.Usuario import UsuarioForm
from lib.d import D
from sqlalchemy.exc import IntegrityError


log = D(debug=True)

usuario = Blueprint('usuario', __name__)

def get_usuarios():
    usuarios = Usuario.query.filter_by(estado='activo').all()
    usuarios = [usuario.serialize() for usuario in usuarios]

    return usuarios

def delete_usuario_by_id(id):
    usuario = Usuario.query.filter_by(id=id).first()
    usuario.estado = 'inactivo'
    db.session.commit()


def update_usuario_by_id(id,form,role):
    usuario = Usuario.query.filter_by(id=id).first()
    usuario.nombre = form.nombre.data
    usuario.apellido = form.apellido.data

    log.info(f'role: {usuario.rol} form: {form.rol.data}')

    if usuario.rol == 'admin' and form.rol.data != 'admin':
        return False
    else:
         usuario.rol = form.rol.data
    if usuario.email != form.email.data:
        usuario.email = form.email.data
    db.session.commit()
    return True

def add_usuario(form):
    try:
        usuario = Usuario(nombre=form.nombre.data, apellido=form.apellido.data, email=form.email.data, password=hash_password(form.password.data), rol=form.rol.data,estado='activo')
        db.session.add(usuario)
        db.session.commit()
        return True
    except IntegrityError as e:
        log.error(e)
        db.session.rollback()
        return False






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
                
            can_edit = update_usuario_by_id(form.id.data, form, token['role'])
            if can_edit:
                flash('Usuario editado correctamente')
            else:
                flash('No puedes cambiar el rol de un administrador', 'danger')
                return render_template('pages/usuario/index.html', form=form, usuarios=get_usuarios(), showModal='false', Mode='edit', errors=None)
        elif 'add' in request.form:
            if not form.validate():
                form.errors.pop('password')

                log.error('Error al agregar el usuario')

                flash('Error al agregar el usuario', 'danger')
                errors = [form.errors[field][0] for field in form.errors]
                log.info(errors)
                return render_template('pages/usuario/index.html', form=form, usuarios=get_usuarios(), showModal='true', Mode='add', errors=errors)
            result = add_usuario(form)
            if result:
                flash('Usuario agregado correctamente')
            else:
                flash('El correo ya está en uso, intenta con otro')
        else:
            flash('Error al procesar la solicitud')
            

    return render_template('pages/usuario/index.html', form=form, usuarios=get_usuarios(), showModal='false', Mode='edit', errors=None)
