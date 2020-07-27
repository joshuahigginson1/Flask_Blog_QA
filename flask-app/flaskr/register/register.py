"""
This file is a template for creating and configuring a blueprint within Flask.

Blueprint Task: Write what the blueprint does HERE.
"""

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, render_template
from flask import current_app as app

# Blueprint Configuration -----------------------------------------------------------------

register_bp = Blueprint(
    'register_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates',
    static_folder='static'
)


# Routes ----------------------------------------------------------------------------------
@register_bp.route('/register', methods=['GET'])
def register_view_function():
    return render_template(
        'register.html',
        title='Register Page',
        subtitle='A page to register new users onto our system.',
        template='register.html'
    )
