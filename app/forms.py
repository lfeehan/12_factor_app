from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea, Select
from wtforms.widgets.html5 import NumberInput


class NameForm(FlaskForm):
    name = StringField(
        'User Name:', validators=[DataRequired(), Length(1, 24)])
    balance = IntegerField(
        'Balance', widget=NumberInput(), validators=[DataRequired()])
    submit = SubmitField('Submit')

"""
    form.name.data = user.name
    form.quantity.data = user.quantity
    form.price_high.data = user.price_high
    form.category.data = user.category
"""