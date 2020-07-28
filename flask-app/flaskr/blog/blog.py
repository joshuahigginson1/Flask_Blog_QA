"""
This file is a template for creating and configuring a blueprint within Flask.
"""

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
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
@login_required
def post_to_blog():
    blog_form = BlogForm()  # Instantiate a NewForm() object, and assign this to a new variable.

    if blog_form.validate_on_submit():
        record = Posts(
            title=blog_form.title.data,
            content=blog_form.content.data,
            author=current_user
        )

        db.session.add(record)
        db.session.commit()

        redirect(url_for('blog_bp.blog_view'))

    return render_template(
        'post_to_blog.html',
        title='Post to Blog Page',
        subtitle='A page for posting articles to our blog',
        template='post_to_blog.html',
        form=blog_form
    )


@blog_bp.route('/blog_view', methods=['GET'])  # Make sure to include post request.
def blog_view():
    blog_form_data = Posts.query.all()  # Request an SQL query and returns this to the blog_form variable.

    return render_template(
        'blog_view.html',
        title='Post to Blog Page',
        subtitle='A page for posting articles to our blog',
        template='blog_view.html',
        blog_posts=blog_form_data
    )
