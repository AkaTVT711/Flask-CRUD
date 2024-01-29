from flask import render_template, redirect, request, url_for, jsonify, flash
from apps import db
from flask_login import current_user, login_required
from . import blueprint
from apps.news.models import News
from apps.news.forms import NewsForm


######### START - API ROUTES #########
@blueprint.route('/api/news', methods=['GET'])
def all_news():
    news_list = News.get_all()  # Call the get_all method to retrieve all news items
    news_data = {
        'status': 200,
        'items': [{"id": news.id, "title": news.title, "content": news.content,
                   "publish_date": news.publish_date.strftime('%Y-%m-%d'), "status": news.status} for news in news_list]
    }
    return jsonify(news_data)


@blueprint.route('/api/news/<int:id>', methods=['GET'])
def edit_news(id):
    news = News.get_by_id(id)
    if news is None:
        return jsonify({"error": "News not found", 'status': 404})
    else:
        if request.method == 'GET':
            return jsonify({"id": news.id, "title": news.title, "content": news.content,
                            "publish_date": news.publish_date.strftime('%Y-%m-%d'), "status": news.status})
    return jsonify({"error": "Something went wrong"})


######### ADMIN ROUTES #########
@blueprint.route('/admin/news')
# @login_required
def index():
    news_list = all_news().get_json()
    if 'items' in news_list:
        response = news_list['items']
    else:
        response = []
    return render_template('business/news/list.html', news_list=response)


@blueprint.route('/admin/news/create', methods=['GET', 'POST'])
# @login_required
def admin_create_news():
    form = NewsForm(request.form)
    try:
        if request.method == 'GET':
            return render_template('business/news/form.html', form=form)

        if request.method == 'POST' and form.validate():
            admin_save_changes(form, new=True)
            flash(' News updated successfully!', 'success')
            return render_template('business/news/form.html', form=form)
    except Exception as e:
        flash(' Error: ' + str(e), 'danger')
    return render_template('business/news/form.html', form=form)


def admin_save_changes(form, id=None, new=False):
    if new:
        News.create(form.data)
    else:
        News.update(form.data, id)


@blueprint.route('/admin/news/<int:id>', methods=['GET', 'POST'])
# @login_required
def admin_edit_news(id):
    try:
        if request.method == 'GET':
            news_detail = edit_news(id).get_json()
        else:
            news_detail = request.form
        form = NewsForm(data=news_detail)

        if request.method == 'POST':
            if form.validate():
                admin_save_changes(form, id)
                flash(' News updated successfully!', 'success')
            else:
                flash(" All fields are required.", 'danger')

        return render_template('business/news/form.html', form=form)
    except Exception as e:
        flash(' Error: ' + str(e), 'danger')
    return render_template('business/news/form.html', form=request.form)


@blueprint.route('/admin/news/view/<int:id>', methods=['GET'])
# @login_required
def admin_view_news(id):
    news_detail = edit_news(id).get_json()
    form = NewsForm(data=news_detail)

    return render_template('business/news/view.html', form=form)


@blueprint.route('/admin/news/delete/<int:id>')
# @login_required
def admin_delete_news(id):
    news_entry = News.query.get(id)
    db.session.delete(news_entry)
    db.session.commit()
    return redirect('/admin/news')

######### END - ADMIN ROUTES #########
