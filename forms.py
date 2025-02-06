from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField, IntegerField, RadioField
from wtforms.validators import InputRequired, Email

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
          'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
          'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
          'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
          'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

class AddSnackForm(FlaskForm):
    """Form fo adding snacks"""

    email = StringField("Email", validators=[Email()])
    name = StringField("Snack Name", validators=[InputRequired(message="Snack name is required")])
    price = FloatField("Price in USD")
    quantity = IntegerField("How many?")
    healthy = BooleanField("Healthy Choice?")

    # category = RadioField("Category", choices=[('appetizer', 'Appetizer'), ('entree', 'Entree'), ('dessert', 'Dessert')])
    category = SelectField("Category", choices=[('appetizer', 'Appetizer'), ('entree', 'Entree'), ('dessert', 'Dessert')])

class EmployeeForm(FlaskForm):

    name = StringField("Employee Name", validators=[InputRequired(message="Name is required")])
    state = SelectField("State", choices=[(state, state) for state in states])
    dept_code = SelectField("Department Code")