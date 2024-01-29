from datetime import datetime
from apps import db


class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    publish_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Boolean, default=False)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def create(cls, data):
        if isinstance(data.get('publish_date'), str):
            publish_date = cls.parse_date(data.get('publish_date'))
        else:
            publish_date = data.get('publish_date')

        new_record = cls(
            title=data.get('title'),
            content=data.get('content'),
            publish_date=publish_date,
            status=data.get('status', False)
        )
        db.session.add(new_record)
        db.session.commit()
        return new_record

    @classmethod
    def update(cls, form, id):
        if not id:
            return None
        news = cls.get_by_id(id)

        news.title = form.get('title')
        news.content = form.get('content')
        news.publish_date = cls.parse_date(form.get('publish_date'))
        news.status = form.get('status', False)
        db.session.commit()
        return cls

    @classmethod
    def parse_date(cls, date_string):
        try:
            return datetime.strptime(date_string, '%Y-%m-%d')
        except ValueError:
            return None
