from wtforms import Form, StringField, SubmitField, IntegerField, BooleanField


class PromoCodesForm(Form):
    id = StringField('Id')
    description = StringField('Description')
    code = StringField('Code')
    status = BooleanField('Status')
    quantity = IntegerField('Quantity')
