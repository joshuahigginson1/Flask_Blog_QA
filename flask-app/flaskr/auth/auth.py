"""
This file is a template for creating and configuring a blueprint within Flask.

Blueprint Task: Stores all routes related to user authentication under auth.py.
"""

# Imports --------------------------------------------------------------------------------
from flask_login import login_user, current_user, login_required, logout_user
from flask import Blueprint, render_template, redirect, url_for
from flaskr import db, bcrypt
from .models import Users
from .forms import RegistrationForm, LoginForm

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

        return redirect(url_for('blog_bp.blog_view'))  # Redirects the user to url/post

    return render_template('register.html',  # Returns render template on html GET req.
                           title='Register',
                           subtitle='Code related to our user registration.',
                           template='register.html',
                           form=reg_form
                           )


@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:  # If the user is already logged in, they don't need to enter details.
        return redirect(url_for('homepage_bp.homepage'))  # Send them back to the homepage.

    log_form = LoginForm()  # Else, instantiate a new login form object.

    if log_form.validate_on_submit():  # If the login form passes validation checks,

        user = Users.query.filter_by(email=log_form.email.data).first()  # Run a query on the submitted email address.

        if user and bcrypt.check_password_hash(user.password, log_form.password.data):  # If there is a user...
            # ... And if bcrypt successfully checks the two password hashes, then:

            login_user(user, remember=log_form.remember.data)  # We login the correct user.
            return redirect(url_for('auth_bp.success'))  # return them to a new page.

        else:
            return redirect(url_for('homepage_bp.homepage'))

    return render_template('login.html', title='Login Page', form=log_form)


@auth_bp.route('/success', methods=['GET'])
@login_required
def success():
    return render_template('success.html', title='SUCCESS! YOU HAVE LOGGED IN!')


@auth_bp.route("/logout", methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))
