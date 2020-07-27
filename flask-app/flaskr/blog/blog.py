"""
This file is a template for creating and configuring a blueprint within Flask.
"""

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, render_template
from flask import current_app as app
from .forms import BlogForm  # import our BlogForm() method.

# Blueprint Configuration -----------------------------------------------------------------

blog_bp = Blueprint(
    'blog_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates',
    static_folder='static'
)


# Routes ----------------------------------------------------------------------------------

@blog_bp.route('/blog_page', methods=['GET', 'POST'])  # Make sure to include post request.
def blog():
    form = BlogForm()  # Instantiate a NewForm() object, and assign this to a new variable.

    return render_template(
        'blog.html',
        title='Blog Page',
        subtitle='Blueprint for code related to our blog specifically.',
        template='blog.html',
        form=form
    )
