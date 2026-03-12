from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Maestros
import forms

maestros_bp = Blueprint("maestros", __name__)

@maestros_bp.route("/maestros", methods=['GET'])
def maestros():
    maestros_list = Maestros.query.all()
    return render_template("maestros.html", maestros=maestros_list)

@maestros_bp.route("/maestros/agregar", methods=['GET', 'POST'])
def agregar():
    create_form = forms.MaestroForm(request.form)
    if request.method == 'POST':
        existe = db.session.query(Maestros).filter(
            Maestros.matricula == create_form.matricula.data
        ).first()
        if existe:
            flash(f"La matrícula {create_form.matricula.data} ya está registrada.", "error")
        else:
            maestro = Maestros(
                matricula=create_form.matricula.data,
                nombre=create_form.nombre.data,
                apellidos=create_form.apellidos.data,
                especialidad=create_form.especialidad.data,
                email=create_form.email.data
            )
            db.session.add(maestro)
            db.session.commit()
            flash("Maestro registrado correctamente.", "success")
            return redirect(url_for('maestros.maestros'))
    return render_template("maestros_agregar.html", form=create_form)

@maestros_bp.route("/maestros/detalles", methods=['GET'])
def detalles():
    id = request.args.get('id')
    maestro = db.session.query(Maestros).filter(Maestros.matricula == id).first()
    if maestro:
        matricula = maestro.matricula
        nombre = maestro.nombre
        apellidos = maestro.apellidos
        especialidad = maestro.especialidad
        email = maestro.email
    else:
        matricula = nombre = apellidos = especialidad = email = ""
    return render_template("maestros_detalles.html", matricula=matricula, nombre=nombre, apellidos=apellidos, especialidad=especialidad, email=email)

@maestros_bp.route("/maestros/modificar", methods=['GET', 'POST'])
def modificar():
    create_form = forms.MaestroForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        maestro = db.session.query(Maestros).filter(Maestros.matricula == id).first()
        if maestro:
            create_form.matricula.data = maestro.matricula
            create_form.nombre.data = maestro.nombre
            create_form.apellidos.data = maestro.apellidos
            create_form.especialidad.data = maestro.especialidad
            create_form.email.data = maestro.email
    if request.method == 'POST':
        id = request.args.get('id')
        maestro = db.session.query(Maestros).filter(Maestros.matricula == id).first()
        if maestro:
            maestro.matricula = create_form.matricula.data
            maestro.nombre = str.rstrip(create_form.nombre.data)
            maestro.apellidos = create_form.apellidos.data
            maestro.especialidad = create_form.especialidad.data
            maestro.email = create_form.email.data
            db.session.add(maestro)
            db.session.commit()
        return redirect(url_for('maestros.maestros'))
    return render_template("maestros_modificar.html", form=create_form, id=request.args.get('id'))

@maestros_bp.route("/maestros/eliminar", methods=['GET', 'POST'])
def eliminar():
    id = request.args.get('id')
    maestro = db.session.query(Maestros).filter(Maestros.matricula == id).first()

    if request.method == 'GET':
        if maestro:
            return render_template("maestros_eliminar.html", maestro=maestro)
        return redirect(url_for('maestros.maestros'))

    if request.method == 'POST':
        if maestro:
            db.session.delete(maestro)
            db.session.commit()
        return redirect(url_for('maestros.maestros'))
