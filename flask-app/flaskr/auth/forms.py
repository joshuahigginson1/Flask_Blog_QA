"""
A template which lays out the basic syntax for a forms.py file using Flask and WTForms.
"""

# Imports --------------------------------------------------------------------------------

from flask_wtf import FlaskForm, RecaptchaField  # Import our Flask Form.
from wtforms import StringField, SubmitField, PasswordField, BooleanField  # Import our field types.
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length  # Import our validators.
from .models import Users
from flask_login import current_user


# Classes --------------------------------------------------------------------------------

class RegistrationForm(FlaskForm):
    email = StringField('Email', [DataRequired(), Email()])

    password = PasswordField('Password', [DataRequired()])

    confirm_password = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])

    first_name = StringField('First Name', [DataRequired(), Length(min=2, max=30)])

    last_name = StringField('Last Name', [DataRequired(), Length(min=3, max=30)])

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


class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name', [DataRequired(), Length(min=4, max=30)])

    last_name = StringField('Last Name', [DataRequired(), Length(min=4, max=30)])

    email = StringField('Email', [DataRequired(), Email()])

    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')
