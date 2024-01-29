from apps import db


class PromoCodes(db.Model):
    __tablename__ = 'promotions'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100))
    description = db.Column(db.Text)
    status = db.Column(db.Boolean, default=False)
    quantity = db.Column(db.Integer)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def create(cls, data):
        new_record = cls(
            code=data.get('code'),
            description=data.get('description'),
            status=data.get('status'),
            quantity=data.get('quantity'),
        )
        db.session.add(new_record)
        db.session.commit()
        return new_record

    @classmethod
    def update(cls, form, id):
        if not id:
            return None
        item = cls.get_by_id(id)

        item.code = form.get('code')
        item.description = form.get('description')
        item.status = form.get('status')
        item.quantity = form.get('quantity')
        db.session.commit()
        return cls
