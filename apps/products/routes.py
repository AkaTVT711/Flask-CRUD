from flask import render_template, redirect, request, url_for
from apps import db
from flask_login import current_user
from . import blueprint
from flask_login import login_required
from apps.products.models import Products


@blueprint.route('/products')
@login_required
def index():
    products_list = Products.query.all()
    return render_template('home/tbl_bootstrap.html', products_list=products_list)


@blueprint.route('/products/create', methods=['GET', 'POST'])
@login_required
def create_products():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        products_entry = products(title=title, content=content)
        db.session.add(products_entry)
        db.session.commit()
        return redirect('/')
    return render_template('create.html')


@blueprint.route('/products/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_products(id):
    products_entry = Products.query.get(id)
    if request.method == 'POST':
        products_entry.title = request.form['title']
        products_entry.content = request.form['content']
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', products_entry=products_entry)


@blueprint.route('/products/delete/<int:id>')
@login_required
def delete_products(id):
    products_entry = Products.query.get(id)
    db.session.delete(products_entry)
    db.session.commit()
    return redirect('/products')
