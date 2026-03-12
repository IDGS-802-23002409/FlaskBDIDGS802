from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Alumnos
import forms

alumnos_bp = Blueprint("alumnos", __name__)

@alumnos_bp.route("/", methods=['GET'])
@alumnos_bp.route("/index", methods=['GET'])
def welcome():
    return render_template("welcome.html")

@alumnos_bp.route("/alumnos", methods=['GET'])
def index():
    alumnos_list = Alumnos.query.all()
    return render_template("index.html", alumno=alumnos_list)

@alumnos_bp.route("/alumnos/agregar", methods=['GET', 'POST'])
def agregar():
    create_form = forms.UserForm2(request.form)
    if request.method == 'POST':
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apaterno=create_form.apellidos.data,
            email=create_form.email.data
        )
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.index'))
    return render_template("alumnos.html", form=create_form)

@alumnos_bp.route("/alumnos/detalles", methods=['GET'])
def detalles():
    id = request.args.get('id')
    alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
    if not alum1:
        return redirect(url_for('alumnos.index'))
    return render_template("detalles.html", alumno=alum1)

@alumnos_bp.route("/alumnos/modificar", methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm2(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        if alum1:
            create_form.id.data = request.args.get('id')
            create_form.nombre.data = alum1.nombre
            create_form.apellidos.data = alum1.apaterno
            create_form.email.data = alum1.email
    if request.method == 'POST':
        id = create_form.id.data
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        if alum1:
            alum1.nombre = str.rstrip(create_form.nombre.data)
            alum1.apaterno = create_form.apellidos.data
            alum1.email = create_form.email.data
            db.session.add(alum1)
            db.session.commit()
        return redirect(url_for('alumnos.index'))
    return render_template("modificar.html", form=create_form, id=request.args.get('id'))

@alumnos_bp.route("/alumnos/eliminar", methods=['GET', 'POST'])
def eliminar():
    id = request.args.get('id')
    alum1 = Alumnos.query.get(id)
    
    if request.method == 'GET':
        if alum1:
            return render_template("alumnos_eliminar.html", alumno=alum1)
        return redirect(url_for('alumnos.index'))
        
    if request.method == 'POST':
        if alum1:
            db.session.delete(alum1)
            db.session.commit()
        return redirect(url_for('alumnos.index'))
