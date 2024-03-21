from flask import Blueprint, render_template, request, redirect, flash
from forms.Login import LoginForm
import smtplib
import jwt
from models.usuario import Usuario
import os
from dotenv import load_dotenv
from email.message import EmailMessage
from models.verificacion import VerificationCode
from db.db import db

from lib.jwt import allowed_roles,token_required,createToken,decodeToken
login = Blueprint('login', __name__, template_folder='templates')
load_dotenv()


@login.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm(request.form)
    token = request.cookies.get('token')
    if token:
        return redirect('/home')

    if request.method == 'POST' and form.validate():
        email = form.correo.data
        contraseña = form.password.data

        # Consultar si el usuario existe
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario:
            if usuario.password == contraseña:
                #guardar como cookie el token
                response = redirect('/enviar_email')
                response.set_cookie('correo', email)
                return response
            else:
                return render_template('pages/login/index.html', form=form)
        else:
            flash('Usuario no existe', 'danger')

        return render_template('pages/login/index.html', form=form)
        
    return render_template('pages/login/index.html', form=form)

@login.route('/enviar_email', methods=['GET', 'POST'])
def enviar_email():
    token = request.cookies.get('token')
    if token:
        return redirect('/home')
    email = request.cookies.get('correo')
    if request.method == 'POST':
        codigo = request.form['codigo']
        verificacion = VerificationCode.query.filter_by(email=email, code=codigo).first()
        if verificacion:
            response = redirect('/home')
            role = Usuario.query.filter_by(email=email).first().rol
            #eliminar el codigo de verificacion
            db.session.delete(verificacion)
            response.set_cookie('token', createToken(email, role))
            return response
        
        else:
            flash('Codigo incorrecto', 'danger')
    verification_code = os.urandom(5).hex()
    verification = VerificationCode(code=verification_code, email=email)
    db.session.add(verification)
    db.session.commit()

    envioEmail(email, 'Prueba', 'Bienvenido, su codigo de verificacion es: '+verification_code)
    return render_template('pages/login/enviar_email.html')



def envioEmail(destinatario, asunto, mensaje):
    email = EmailMessage()
    email['From'] = os.getenv('EMAIL')
    email['To'] = destinatario
    email['Subject'] = asunto
    email.set_content(mensaje)

    smtp = smtplib.SMTP_SSL('smtp.gmail.com')
    smtp.login(os.getenv('EMAIL'), os.getenv('PASSWORD_EMAIL'))
    smtp.send_message(email)
    smtp.quit()

@login.route('/404')
def not_found():
    return "Not found", 404



@login.route('/logout')
def logout():
    response = redirect('/login')
    response.set_cookie('token', '', expires=0)
    return response

