"""
This file is a template for creating and configuring a blueprint within Flask.
"""

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, render_template, current_app as app
from flaskr import db
from .forms import BlogForm  # import our BlogForm() method.
from .models import Posts

# Blueprint Configuration -----------------------------------------------------------------

blog_bp = Blueprint(
    'blog_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates',
    static_folder='static'
)


# Routes ----------------------------------------------------------------------------------

@blog_bp.route('/post_to_blog', methods=['GET', 'POST'])  # Make sure to include post request.
def post_to_blog():
    blog_form = BlogForm()  # Instantiate a NewForm() object, and assign this to a new variable.

    if blog_form.validate_on_submit():
        record = Posts(
            first_name=blog_form.first_name.data,
            last_name=blog_form.last_name.data,
            title=blog_form.title.data,
            content=blog_form.content.data
        )

        db.session.add(record)
        db.session.commit()

    return render_template(
        'post_to_blog.html',
        title='Post to Blog Page',
        subtitle='A page for posting articles to our blog',
        template='post_to_blog.html',
        form=blog_form
    )


@blog_bp.route('/blog_view', methods=['GET'])  # Make sure to include post request.
def blog_view():

    blog_form_data = Posts.query.first()  # Request an SQL query and return this to the blog_form variable.

    return render_template(
        'blog_view.html',
        title='Post to Blog Page',
        subtitle='A page for posting articles to our blog',
        template='blog_view.html',
        blog_data=blog_form_data
    )
