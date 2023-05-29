from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

# CRUD models
from flaskapp.models.crud_model import Crud_tbl


class Basic_post(FlaskForm):
    s_str  = StringField('str_f', validators=[DataRequired()])
    s_txt  = TextAreaField('text_f', validators=[DataRequired()])
    s_int  = IntegerField('integer_f', validators=[DataRequired()])
    submit = SubmitField('Register', validators=[DataRequired()]) 


