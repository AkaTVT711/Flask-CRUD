from flask_ckeditor import CKEditorField
from wtforms import Form, StringField, SubmitField, DateField, BooleanField


class NewsForm(Form):
    id = StringField('Id')
    title = StringField('Title')
    content = CKEditorField('Content')
    publish_date = DateField('Publish Date')
    status = BooleanField('Status')
