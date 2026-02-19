from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, BooleanField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id=IntegerField("id", [validators.DataRequired("El campo es requerido"),
                                        validators.NumberRange(min=100, max=1000, message="Ingrese un valor valido")])
    nombre=StringField("Nombre", [validators.DataRequired("El campo es requerido"),
                                validators.length(min=3, max=10, message="ingrese un nombre netre 2 y 10 caracteres")])
    apaterno=StringField("Apaterno", [validators.DataRequired("El campo es requerido")])
    correo=EmailField("Correo", [validators.email("El email es requerido")])
