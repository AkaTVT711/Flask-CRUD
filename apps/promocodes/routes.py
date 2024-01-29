from flask import render_template, redirect, request, url_for, jsonify, flash
from apps import db
from flask_login import current_user, login_required
from . import blueprint
from apps.promocodes.models import PromoCodes
from apps.promocodes.forms import PromoCodesForm


######### START - API ROUTES #########
@blueprint.route('/api/promo-codes', methods=['GET'])
def all_promo_codes():
    promo_codes_list = PromoCodes.get_all()  # Call the get_all method to retrieve all promo-codes items
    promo_codes_data = {
        'status': 200,
        'items': [{"id": item.id, "code": item.code, "description": item.description, "status": item.status,
                   "quantity": item.quantity} for item in promo_codes_list]
    }
    return jsonify(promo_codes_data)


@blueprint.route('/api/promo-codes/<int:id>', methods=['GET'])
def edit_promo_codes(id):
    item = PromoCodes.get_by_id(id)
    if item is None:
        return jsonify({"error": "Promo-Codes not found", 'status': 404})
    else:
        if request.method == 'GET':
            return jsonify({"id": item.id, "code": item.code, "description": item.description, "status": item.status,
                            "quantity": item.quantity})
    return jsonify({"error": "Invalid request method"})


######### ADMIN ROUTES #########
@blueprint.route('/admin/promo-codes')
# @login_required
def index():
    promo_codes_list = all_promo_codes().get_json()
    if 'items' in promo_codes_list:
        response = promo_codes_list['items']
    else:
        response = []
    return render_template('business/promo-codes/list.html', promo_codes_list=response)


@blueprint.route('/admin/promo-codes/create', methods=['GET', 'POST'])
# @login_required
def admin_create_promo_codes():
    form = PromoCodesForm(request.form)
    try:
        if request.method == 'GET':
            return render_template('business/promo-codes/form.html', form=form)

        if request.method == 'POST' and form.validate():
            admin_save_changes(form, new=True)
            flash(' Item updated successfully!', 'success')
            return render_template('business/promo-codes/form.html', form=form)
    except Exception as e:
        flash(' Error: ' + str(e), 'danger')
    return render_template('business/promo-codes/form.html', form=form)


def admin_save_changes(form, id=None, new=False):
    if new:
        PromoCodes.create(form.data)
    else:
        PromoCodes.update(form.data, id)


@blueprint.route('/admin/promo-codes/<int:id>', methods=['GET', 'POST'])
# @login_required
def admin_edit_promo_codes(id):
    try:
        if request.method == 'GET':
            promocodes_detail = edit_promo_codes(id).get_json()
        else:
            promocodes_detail = request.form
        form = PromoCodesForm(data=promocodes_detail)

        if request.method == 'POST':
            if form.validate():
                admin_save_changes(form, id)
                flash(' Item updated successfully!', 'success')
            else:
                flash(" All fields are required.", 'danger')

        return render_template('business/promo-codes/form.html', form=form)
    except Exception as e:
        flash(' Error: ' + str(e), 'danger')
    return render_template('business/promo-codes/form.html', form=request.form)


@blueprint.route('/admin/promo-codes/view/<int:id>', methods=['GET'])
# @login_required
def admin_view_promo_codes(id):
    promocodes_detail = edit_promo_codes(id).get_json()
    form = PromoCodesForm(data=promocodes_detail)

    return render_template('business/promo-codes/view.html', form=form)


@blueprint.route('/admin/promo-codes/delete/<int:id>')
# @login_required
def admin_delete_promo_codes(id):
    promocodes_entry = PromoCodes.query.get(id)
    db.session.delete(promocodes_entry)
    db.session.commit()
    return redirect('/admin/promo-codes')

######### END - ADMIN ROUTES #########
