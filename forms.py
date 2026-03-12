from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, EmailField, RadioField
from wtforms import validators
from wtforms.validators import DataRequired, NumberRange    


class UserForm2(FlaskForm): 
    id = IntegerField('Id', [
        validators.Optional()
    ])
    nombre = StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un nombre valido")
    ])
    apellidos = StringField('Apellidos', [
        validators.DataRequired(message="El campo es requerido")
    ])
    amaterno = StringField('Amaterno', [
    validators.Optional()   
    ])
    email = EmailField('Correo', [
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="Correo no valido")
    ])
    telefono=StringField("telefono",[
        validators.DataRequired(message="El telefono es requerido"),
        validators.DataRequired(message="Ingrese un telefono valido")
    ])
    
class MaestroForm(FlaskForm):
    matricula = IntegerField('Matrícula', validators=[validators.DataRequired()])
    nombre = StringField('Nombre', validators=[validators.DataRequired()])
    apellidos = StringField('Apellidos', validators=[validators.DataRequired()])
    especialidad = StringField('Especialidad', validators=[validators.DataRequired()])
    email = EmailField('Correo Electrónico', validators=[validators.DataRequired(), validators.Email()])

class CursoForm(FlaskForm):
    nombre = StringField('Nombre del Curso', validators=[validators.DataRequired(), validators.length(max=150)])
    descripcion = StringField('Descripción', validators=[validators.Optional()])
    maestro_id = IntegerField('Matrícula del Maestro', validators=[validators.DataRequired()])

class InscripcionForm(FlaskForm):
    alumno_id = IntegerField('ID del Alumno', validators=[validators.DataRequired()])
