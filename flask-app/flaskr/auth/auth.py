"""
This file is a template for creating and configuring a blueprint within Flask.

Blueprint Task: Stores all routes related to user authentication under auth.py.
"""

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, render_template, redirect, url_for
from flaskr import db, bcrypt
from .models import Users
from .forms import RegistrationForm

# Blueprint Configuration -----------------------------------------------------------------

auth_bp = Blueprint(
    'auth_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates',
    static_folder='static'
)


# Routes ----------------------------------------------------------------------------------

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():

    reg_form = RegistrationForm()  # Instantiate a new instance of RegistrationForm().

    if reg_form.validate_on_submit():  # If the data passes WTForms validation, then:
        hash_pw = bcrypt.generate_password_hash(reg_form.password.data)  # Before we add, hash our password.

        user = Users(email=reg_form.email.data, password=hash_pw)  # Set user and pass to an instance of Users().

        db.session.add(user)  # Add Users object to our session.
        db.session.commit()  # Commit data to our database.

        return redirect(url_for('blog_view'))  # Redirects the user to url/post

    return render_template('register.html',  # Returns render template on html GET req.
                           title='Register',
                           subtitle='Code related to our user registration.',
                           template='register.html',
                           form=reg_form
                           )
