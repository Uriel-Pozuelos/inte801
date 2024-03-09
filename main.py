from flask import Flask,render_template,Blueprint
from routes.home.index import home


app = Flask(__name__)

app.register_blueprint(home)


@app.route('/')
def index():
    return render_template('pages/index.html')




if __name__ == '__main__':
    app.run(debug=True)