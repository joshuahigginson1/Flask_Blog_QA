"""
This file is a template for creating and configuring a blueprint within Flask.

Blueprint Task: Stores all routes related to user authentication under auth.py.
"""

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, render_template
from flask import current_app as app

# Blueprint Configuration -----------------------------------------------------------------

auth_bp = Blueprint(
    'auth_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates',
    static_folder='static'
)

# Routes ----------------------------------------------------------------------------------
@auth_bp.route('/url', methods=['GET'])
def new_view_function():
    return render_template(
        '<LOCATION OF TEMPLATE.HTML>',
        title='Flask Blueprint Demo',
        subtitle='Demonstration of Flask blueprints in action.',
        template='new-template',
    )
