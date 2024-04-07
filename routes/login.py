from flask import Blueprint, render_template, request, redirect, flash,g
from forms.Login import LoginForm
from forms.ResetPassword import ResetPasswordForm
from models.usuario import Usuario,loginLog
from models.histDB import PasswordHistories
from dotenv import load_dotenv
from db.db import db
import datetime
from lib.d import D
from lib.jwt import allowed_roles,token_required,createToken,decodeToken,hash_password
login = Blueprint('login', __name__, template_folder='templates')
load_dotenv()

log = D(debug=True)

TIME_TO_BLOCK = 0.1

def save_login_log(user_id, estado):
    login_log = loginLog(user_id=user_id, estado=estado)
    db.session.add(login_log)
    db.session.commit()

def user_is_blocked(user):
    if user.is_blocked:
        if user.blocked_until:
            return True
        else:
            return False
    else:
        return False
    

def block_user_until(user, minutes):
    user.is_blocked = True
    user.blocked_until = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
    db.session.commit()

def unblock_user(user):
    try:
        user.is_blocked = False
        user.blocked_until = None
        db.session.commit()
        return True
    except Exception as e:
        log.error(e)
        return False

def check_user_blocked(user):
    
    if user.is_blocked:
        if user.blocked_until:
            if user.blocked_until < datetime.datetime.now():
                unblock_user(user)
            else:
                return True
        else:
            return False
    else:
        return False
    
def unban_user(user):
    #si la fecha actual es mayor a la fecha de desbloqueo, se desbloquea el usuario
    if user.blocked_until < datetime.datetime.now():
        user.is_blocked = 0
        user.blocked_until = None
        db.session.commit()
        return True
    else:
        return False
    
def check_last_logins(user, intentos):
    last_logins = loginLog.query.filter_by(user_id=user.id).order_by(loginLog.fecha_login.desc()).limit(intentos).all()
    
    if len(last_logins) == 3:
        if all(login.estado == 'incorrecto' for login in last_logins):
            block_user_until(user, TIME_TO_BLOCK)
            return True
        else:
            return False
    elif user.is_blocked == 1:  # Usuario está bloqueado
        log.info('Usuario bloqueado')
        current_time = datetime.now()
        print(current_time)
        if current_time > user.blocked_until:
            # Eliminar el estado de bloqueo
            user.is_blocked = 0
            user.blocked_until = None
            db.session.commit()
            return False  # No está bloqueado, se puede proceder
        else:
            return True  # Usuario aún está bloqueado
    else:
        return False  # No cumple con las condiciones para bloqueo

def get_last_login_time(user):
    last_login = loginLog.query.filter_by(user_id=user.id).order_by(loginLog.fecha_login.desc()).first()
    return last_login.fecha_login

@login.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm(request.form)
    token = request.cookies.get('token')
    if token:
        # validar que el token no haya expirado
        try:
            decodeToken(token)
        except Exception as e:
            print(e)
            flash('Tu sesión ha expirado. Por favor inicia sesión de nuevo', 'danger')
            #quito la cookie
            response = redirect('/login')
            response.set_cookie('token', '', expires=0)
            return response
        return redirect('/home')

    if request.method == 'POST' and form.validate():
        email = form.correo.data
        contraseña = hash_password(form.password.data)

        # Consultar si el usuario existe
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario:
            # Verificar si el usuario está bloqueado
            if check_user_blocked(usuario):
                is_unblocked = unban_user(usuario)
                if is_unblocked is False:
                    flash('Tu cuenta está bloqueada. Intenta más tarde.', 'danger')
                    return render_template('pages/login/index.html', form=form)
                else:
                    flash('Tu cuenta ha sido desbloqueada', 'success')
                    return render_template('pages/login/index.html', form=form)
            
            #advertir al usuario que su cuenta esta bloqueada
            if check_last_logins(usuario, 2):
                flash(f'Advertencia: Si fallas el siguiente intento de inicio de sesión, tu cuenta será bloqueada por {TIME_TO_BLOCK} minutos', 'warning')
                return render_template('pages/login/index.html', form=form)

            # Verificar si los últimos tres logins fueron incorrectos
            if check_last_logins(usuario, 3):
                is_unblocked = unban_user(usuario)
                if is_unblocked is False:
                    flash(f'Tu cuenta ha sido bloqueada debido a múltiples intentos fallidos de inicio de sesión. Intenta en {TIME_TO_BLOCK} minutos', 'danger')
                    return render_template('pages/login/index.html', form=form)

            if usuario.password == contraseña:
                # Guardar como cookie el token
                print('-------------------------------------')
                response = redirect('/home')
                token = createToken(email, usuario.rol)
                response.set_cookie('token', token)

                # Guardar en la tabla login_log
                save_login_log(usuario.id, 'correcto')

                #mostrar un flash con la fecha y hora del ultimo inicio de sesion
                last_login = get_last_login_time(usuario)
                flash(f'Bienvenido de vuelta. Tu último inicio de sesión fue el {last_login}', 'success')
                return response
            else:
                flash('Usuario o contraseña incorrectos', 'danger')
                # Guardar en la tabla login_log
                save_login_log(usuario.id, 'incorrecto')

                return render_template('pages/login/index.html', form=form)
        else:
            # Guardar en la tabla login_log
            save_login_log(0, 'incorrecto')
            flash('Usuario no existe', 'danger')

        return render_template('pages/login/index.html', form=form)
        
    return render_template('pages/login/index.html', form=form)


@login.route('/resetPassword', methods=['GET', 'POST'])
def reset_password():
    form = ResetPasswordForm(request.form)
    try:
        token = request.cookies.get('token')
        if token:
            return redirect('/home')

        email = form.correo.data
        password = hash_password(form.password.data)
        confirm_password = hash_password(form.confirm_password.data)

        if request.method == 'POST':
            usuario = Usuario.query.filter_by(email=email).first()
            if not usuario:
                flash('Usuario no existe', 'danger')
            elif password != confirm_password:
                flash('Las contraseñas no coinciden', 'danger')
            else:
                can_continue = PasswordHistories.query.filter_by(user_id=usuario.id, password=password).all()
                if can_continue:
                    flash('La contraseña ya ha sido utilizada anteriormente', 'danger')
                else:
                    usuario.password = password
                    db.session.commit()
                    return redirect('/login')
        
    except Exception as e:
        print(e)
        flash('Error al enviar el email', 'danger')

    return render_template('pages/login/enviar_email.html', form=form)





@login.route('/404')
def not_found():
    if g.rol == 'invitado':
        return render_template('pages/404/404.html'), 404
    return render_template('pages/404/404log.html'), 404



@login.route('/logout')
def logout():
    response = redirect('/login')
    response.set_cookie('token', '', expires=0)
    return response

