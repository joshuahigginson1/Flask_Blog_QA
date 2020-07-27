"""
A template which lays out the basic syntax for a forms.py file using Flask and  WTForms.
"""

# Imports --------------------------------------------------------------------------------

from flask_wtf import FlaskForm, RecaptchaField  # Import our Flask Form.
from wtforms import StringField, SubmitField  # Import our field types.
from wtforms.validators import DataRequired, Length, Email  # Import our validators.


# Classes --------------------------------------------------------------------------------

class BlogForm(FlaskForm):
    first_name = StringField('First Name', [
        Length(min=2, max=30),
        DataRequired()])

    last_name = StringField('Last Name', [
        Length(min=2, max=30),
        DataRequired()])

    title = StringField('Title', [
        Length(min=2, max=100),
        DataRequired()])

    content = StringField('Content', [
        Length(min=2, max=500),
        DataRequired()])

    submit = SubmitField('Continue')

# Validator Syntax:
# VARIABLE = FIELD_TYPE('FIELD_NAME', [ # list of validators.
# VALIDATOR_TYPE(message=('ERROR_MESSAGE'),
# VALIDATOR_TYPE(message=('ERROR_MESSAGE')
# )])
