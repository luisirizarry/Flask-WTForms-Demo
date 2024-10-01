from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField

class AddSnackForm(FlaskForm):
    """Form fo adding snacks"""

    name = StringField("Snack Name")
    price = FloatField("Price in USD")