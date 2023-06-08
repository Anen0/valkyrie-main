from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, EmailField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

# CRUD models
from flaskapp.models.crud_model import job_application

from flaskapp import run_dammit
app = run_dammit()


class Basic_post(FlaskForm):
    s_str  = StringField('str_f', validators=[DataRequired()])
    s_txt  = TextAreaField('text_f', validators=[DataRequired()])
    s_int  = IntegerField('integer_f', validators=[DataRequired()])
    submit = SubmitField('Register', validators=[DataRequired()]) 


class input_forms_job(FlaskForm):
    first_name      = StringField('First Name', validators=[DataRequired()])
    mid_name        = StringField('Middle Name')
    last_name       = StringField('Last Name', validators=[DataRequired()])
    datepicker      = StringField('Date Of Birth', validators=[DataRequired()])
    street_add      = StringField('Street Address', validators=[DataRequired()])
    street_add_two  = StringField('Street Address 2')
    city            = StringField('City', validators=[DataRequired()])
    province        = StringField('Province', validators=[DataRequired()])
    zip_code        = StringField('Zip Code', validators=[DataRequired()])
    email           = EmailField('Email', validators=[DataRequired(), Email()])
    phone_num       = StringField('Phone Number', validators=[DataRequired(), Length(min=13, max=13)])
    linkedin        = StringField('LinkedIn')
    file_input      = FileField('Upload Resume', validators=[FileRequired(), FileAllowed(app.config['ALLOWED_EXTENSIONS'])])

    submit = SubmitField('Submit Application', validators=[DataRequired()]) 

