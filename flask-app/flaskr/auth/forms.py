"""
A template which lays out the basic syntax for a forms.py file using Flask and WTForms.
"""

# Imports --------------------------------------------------------------------------------

from flask_wtf import FlaskForm, RecaptchaField  # Import our Flask Form.
from wtforms import StringField, SubmitField, PasswordField, BooleanField  # Import our field types.
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError  # Import our validators.
from .models import Users


# Classes --------------------------------------------------------------------------------

class RegistrationForm(FlaskForm):
    email = StringField('Email', [DataRequired(), Email()])

    password = PasswordField('Password', [DataRequired()])

    confirm_password = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')


class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired(), Email()])

    password = PasswordField('Password', [DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')
