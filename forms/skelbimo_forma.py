from wtforms import StringField, TextAreaField, SelectField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from .category import categories
from flask_wtf.file import FileField


class AuctionForm(FlaskForm):
    title = StringField("Skelbimo pavadinimas:", validators=[InputRequired()])
    category = SelectField('Category', choices=categories.value())
    city = StringField("Miestas", validators=[InputRequired()])
    price = IntegerField("Kaina", validators=[InputRequired()])
    image = FileField("Skelbimo nuotrauka")
    description = TextAreaField("Aprasymas", validators=[InputRequired()])