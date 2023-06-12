from flask import Blueprint, render_template, url_for, flash, redirect
from DarkTech.forms import PostForm
from .models import Post # import db from models.py
from . import db # import db from __init__.py

main = Blueprint('main', __name__)

@main.route('/')
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

@main.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@main.route('/post/new', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form)

@main.route('/admin')
def admin():
    return render_template('admin.html')

@main.route('/admin/users')
def admin_users():
    # Here you could fetch data from your database and pass it to the template
    # users = get_all_users()
    # return render_template('admin_users.html', users=users)
    return render_template('admin_users.html')
