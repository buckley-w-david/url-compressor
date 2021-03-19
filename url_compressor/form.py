from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import URL, DataRequired

class CompressorForm(FlaskForm):
    url = StringField('url', validators=[URL()])
