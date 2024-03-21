from flask import Blueprint, render_template, request, redirect, url_for, flash



login = Blueprint('login', __name__, template_folder='templates')


@login.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        return render_template('pages/login/index.html')