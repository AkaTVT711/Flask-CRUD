from datetime import datetime
from apps import db


class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    published_date = db.Column(db.DateTime, default=datetime.utcnow)
