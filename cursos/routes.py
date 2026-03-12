from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Curso, Maestros, Alumnos, Inscripcion
import forms

cursos_bp = Blueprint("cursos", __name__)


@cursos_bp.route("/cursos", methods=['GET'])
def index():
    cursos_list = Curso.query.all()
    return render_template("cursos.html", cursos=cursos_list)


@cursos_bp.route("/cursos/agregar", methods=['GET', 'POST'])
def agregar():
    form = forms.CursoForm(request.form)
    maestros_list = Maestros.query.all()
    if request.method == 'POST':
        curso = Curso(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            maestro_id=form.maestro_id.data
        )
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for('cursos.index'))
    return render_template("cursos_agregar.html", form=form, maestros=maestros_list)


@cursos_bp.route("/cursos/detalles", methods=['GET'])
def detalles():
    id = request.args.get('id')
    curso = Curso.query.get(id)
    if not curso:
        return redirect(url_for('cursos.index'))
    return render_template("cursos_detalles.html", curso=curso)


@cursos_bp.route("/cursos/modificar", methods=['GET', 'POST'])
def modificar():
    form = forms.CursoForm(request.form)
    maestros_list = Maestros.query.all()
    id = request.args.get('id')
    curso = Curso.query.get(id)

    if request.method == 'GET' and curso:
        form.nombre.data = curso.nombre
        form.descripcion.data = curso.descripcion
        form.maestro_id.data = curso.maestro_id

    if request.method == 'POST' and curso:
        curso.nombre = form.nombre.data
        curso.descripcion = form.descripcion.data
        curso.maestro_id = form.maestro_id.data
        db.session.commit()
        return redirect(url_for('cursos.index'))

    return render_template("cursos_modificar.html", form=form, maestros=maestros_list, id=id)


@cursos_bp.route("/cursos/eliminar", methods=['GET', 'POST'])
def eliminar():
    id = request.args.get('id')
    curso = Curso.query.get(id)

    if request.method == 'GET':
        if curso:
            return render_template("cursos_eliminar.html", curso=curso)
        return redirect(url_for('cursos.index'))

    if request.method == 'POST':
        if curso:
            db.session.delete(curso)
            db.session.commit()
        return redirect(url_for('cursos.index'))


@cursos_bp.route("/cursos/inscribir", methods=['GET', 'POST'])
def inscribir():
    id = request.args.get('id')
    curso = Curso.query.get(id)
    if not curso:
        return redirect(url_for('cursos.index'))

    alumnos_list = Alumnos.query.all()
    inscritos_ids = [a.id for a in curso.alumnos]

    if request.method == 'POST':
        alumno_id = request.form.get('alumno_id')
        alumno = Alumnos.query.get(alumno_id)
        if alumno and alumno not in curso.alumnos:
            curso.alumnos.append(alumno)
            db.session.commit()
        return redirect(url_for('cursos.detalles', id=id))

    return render_template("cursos_inscribir.html", curso=curso, alumnos=alumnos_list, inscritos_ids=inscritos_ids)


@cursos_bp.route("/cursos/desinscribir", methods=['POST'])
def desinscribir():
    curso_id = request.form.get('curso_id')
    alumno_id = request.form.get('alumno_id')
    curso = Curso.query.get(curso_id)
    alumno = Alumnos.query.get(alumno_id)
    if curso and alumno and alumno in curso.alumnos:
        curso.alumnos.remove(alumno)
        db.session.commit()
    return redirect(url_for('cursos.detalles', id=curso_id))
