from flask_ckeditor import CKEditorField
from wtforms import Form, StringField, SubmitField, DateField, BooleanField, IntegerField, DecimalField


class ProductsForm(Form):
    id = StringField('Id')
    name = StringField('Name')
    description = CKEditorField('Description')
    price = DecimalField('Price')
    stock = IntegerField('Stock')
