from flask import render_template, redirect, request, url_for
from apps import db
from flask_login import current_user
from . import blueprint
from flask_login import login_required
from apps.news.models import News


@blueprint.route('/news')
@login_required
def index():
    news_list = News.query.all()
    return render_template('home/tbl_bootstrap.html', news_list=news_list)


@blueprint.route('/news/create', methods=['GET', 'POST'])
@login_required
def create_news():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        news_entry = News(title=title, content=content)
        db.session.add(news_entry)
        db.session.commit()
        return redirect('/')
    return render_template('create.html')


@blueprint.route('/news/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    news_entry = News.query.get(id)
    if request.method == 'POST':
        news_entry.title = request.form['title']
        news_entry.content = request.form['content']
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', news_entry=news_entry)


@blueprint.route('/news/delete/<int:id>')
@login_required
def delete_news(id):
    news_entry = News.query.get(id)
    db.session.delete(news_entry)
    db.session.commit()
    return redirect('/news')
