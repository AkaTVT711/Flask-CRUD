from apps import db


class Products(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    price = db.Column(db.DECIMAL)
    stock = db.Column(db.Integer)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def create(cls, data):
        new_record = cls(
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price'),
            stock=data.get('stock'),
        )
        db.session.add(new_record)
        db.session.commit()
        return new_record

    @classmethod
    def update(cls, form, id):
        if not id:
            return None
        item = cls.get_by_id(id)

        item.name = form.get('name')
        item.description = form.get('description')
        item.price = form.get('price')
        item.stock = form.get('stock')
        db.session.commit()
        return cls
