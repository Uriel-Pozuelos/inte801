from functools import wraps
from flask import request,redirect,url_for
import jwt
import os
import dotenv
from datetime import datetime, timedelta
envs = dotenv.dotenv_values()

"""
Decorador para verificar el token en las cookies

"""

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')

        if not token:
            return redirect(url_for('login.not_found')) #redirige a la pagina de login si no hay token
        try:
            data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
            #si el token es valido, se ejecuta la funcion
            return f(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return redirect(url_for('login.not_found'), message="Token expirado")
        except jwt.InvalidTokenError:
            return redirect(url_for('login.not_found'), message="Token invalido")
    return decorated


"""
Decorador para verficar los roles y permitir o negar el acceso a las rutas
"""
def allowed_roles(roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.cookies.get('token')
            if not token:
                return redirect(url_for('login'))
            try:
                data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
                if data['role'] not in roles:
                    return redirect(url_for('login.not_found'))
                return f(*args, **kwargs)
            except jwt.ExpiredSignatureError:
                return redirect(url_for('login.not_found'), message="Token expirado")
            except jwt.InvalidTokenError:
                return redirect(url_for('login.not_found'), message="Token invalido")
        return decorated_function
    return decorator


"""
funcion para crear el token
"""
def createToken(email, role):
    # Calcula la fecha y hora actuales
    now = datetime.utcnow()

    # Define el tiempo de expiración (1 hora desde ahora)
    expiration = now + timedelta(hours=1)

    # Crea el payload del token con 'email', 'role' y 'exp'
    payload = {
        'email': email,
        'role': role,
        'exp': expiration,
    }

    # Codifica el token con la clave secreta y el algoritmo
    token = jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm='HS256')
    return token


"""
funcion para decodificar el token
"""

def decodeToken(token):
    return jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])


"""
decorador para que en caso de haber sesion, no se pueda acceder a la pagina de login y regrese a la ultima pagina visitada
"""
def negate_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        #saber de que pagina viene
        last_page = request.referrer
        if token:
            return redirect(last_page)
        return f(*args, **kwargs)
    return decorated
