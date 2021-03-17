from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField


class RegisterForm(FlaskForm):
    first_name = StringField("Iveskite varda", validators=[DataRequired()])
    last_name = StringField("Iveskite pavarde", validators=[DataRequired()])
    email = EmailField("Iveskite elektronini pasta", validators=[DataRequired(), Email()])
    username = StringField("Iveskiteprisijungimo vardas", validators=[DataRequired()])
    password = PasswordField("Iveskite slaptazodi", validators=[DataRequired()])