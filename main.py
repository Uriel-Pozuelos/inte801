from flask import Flask,render_template,Blueprint
from routes.home.index import home
from dotenv import load_dotenv
# from config import DevConfig
from flask_wtf.csrf import CSRFProtect

load_dotenv()



app = Flask(__name__)
# app.config.from_object(DevConfig)
csrf = CSRFProtect(app)
app.register_blueprint(home)


@app.route('/')
def index():
    return render_template('pages/index.html')




if __name__ == '__main__':
    app.run(debug=True)