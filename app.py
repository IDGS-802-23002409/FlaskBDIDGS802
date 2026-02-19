from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
from models import db
from models import Alumnos


app = Flask(__name__)
app.config.form_object(DevelopmentConfig)
db.init_app(app)
csrf=CSRFProtect()


@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/alumnos")
def alumnos():
    return render_template("Alumnos.html")

@app.errorhandler(404)
def page_not_fount(e):
    return render_template("404.html"),404


if __name__ == '__main__':
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
app.run(debug=True)
