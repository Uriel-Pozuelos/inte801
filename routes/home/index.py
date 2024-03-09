from flask import Blueprint, render_template


home = Blueprint('home', __name__, template_folder='templates')

@home.route('/')
def index():
    return render_template('pages/home/index.html')


@home.route('/login')
def login():
    return render_template('pages/login/index.html')