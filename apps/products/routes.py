from flask import render_template, redirect, request, url_for, jsonify, flash
from apps import db
from flask_login import current_user, login_required
from . import blueprint
from apps.products.models import Products
from apps.products.forms import ProductsForm


######### START - API ROUTES #########
@blueprint.route('/api/products', methods=['GET'])
def all_products():
    products_list = Products.get_all()  # Call the get_all method to retrieve all products items
    products_data = {
        'status': 200,
        'items': [{"id": products.id, "name": products.name, "description": products.description,
                   "price": products.price, "stock": products.stock} for products in products_list]
    }
    return jsonify(products_data)


@blueprint.route('/api/products/<int:id>', methods=['GET'])
def edit_products(id):
    products = Products.get_by_id(id)
    if products is None:
        return jsonify({"error": "Products not found", 'status': 404})
    else:
        if request.method == 'GET':
            return jsonify({"id": products.id, "name": products.name, "description": products.description,
                            "price": products.price, "stock": products.stock})
    return jsonify({"error": "Invalid request method"})


######### ADMIN ROUTES #########
@blueprint.route('/admin/products')
# @login_required
def index():
    products_list = all_products().get_json()
    if 'items' in products_list:
        response = products_list['items']
    else:
        response = []
    return render_template('business/products/list.html', products_list=response)


@blueprint.route('/admin/products/create', methods=['GET', 'POST'])
# @login_required
def admin_create_products():
    form = ProductsForm(request.form)
    try:
        if request.method == 'GET':
            return render_template('business/products/form.html', form=form)

        if request.method == 'POST' and form.validate():
            admin_save_changes(form, new=True)
            flash(' Item updated successfully!', 'success')
            return render_template('business/products/form.html', form=form)
    except Exception as e:
        flash(' Error: ' + str(e), 'danger')
    return render_template('business/products/form.html', form=form)


def admin_save_changes(form, id=None, new=False):
    if new:
        Products.create(form.data)
    else:
        Products.update(form.data, id)


@blueprint.route('/admin/products/<int:id>', methods=['GET', 'POST'])
# @login_required
def admin_edit_products(id):
    try:
        if request.method == 'GET':
            products_detail = edit_products(id).get_json()
        else:
            products_detail = request.form
        form = ProductsForm(data=products_detail)

        if request.method == 'POST':
            if form.validate():
                admin_save_changes(form, id)
                flash(' Item updated successfully!', 'success')
            else:
                flash(" All fields are required.", 'danger')

        return render_template('business/products/form.html', form=form)
    except Exception as e:
        flash(' Error: ' + str(e), 'danger')
    return render_template('business/products/form.html', form=request.form)


@blueprint.route('/admin/products/view/<int:id>', methods=['GET'])
# @login_required
def admin_view_products(id):
    products_detail = edit_products(id).get_json()
    form = ProductsForm(data=products_detail)

    return render_template('business/products/view.html', form=form)


@blueprint.route('/admin/products/delete/<int:id>')
# @login_required
def admin_delete_products(id):
    products_entry = Products.query.get(id)
    db.session.delete(products_entry)
    db.session.commit()
    return redirect('/admin/products')

######### END - ADMIN ROUTES #########
