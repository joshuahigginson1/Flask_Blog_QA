"""
This file is a template for creating and configuring a blueprint within Flask.
"""

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, render_template
from flask import current_app as app

# Blueprint Configuration -----------------------------------------------------------------

homepage_bp = Blueprint(
    'homepage_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates',
    static_folder='static'
)


# Routes ----------------------------------------------------------------------------------
@homepage_bp.route('/', methods=['GET'])
@homepage_bp.route('/home', methods=['GET'])
def homepage():
    nav_bar = [
        {'name': 'Home Page', 'url': "url_for('homepage_bp.homepage')"},
        {'name': 'About Page', 'url': "url_for('about')"},
        {'name': 'Register Page', 'url': "url_for('register')"},
        {'name': 'Blog Page', 'url': "url_for('blog_bp.blog')"}
    ]

    return render_template('homepage.html',
                           title='Home Page',
                           subtitle='Homepage Blueprint',
                           template='homepage.html')
