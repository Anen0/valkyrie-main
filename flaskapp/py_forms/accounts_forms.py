from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

# Account related models
from flaskapp.models.accounts_model import User_accnt 



# REGISTER PAGE
class RegisterForm(FlaskForm):
    email               = StringField('Email', validators=[DataRequired(), Email()])
    username            = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password            = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=50)])
    confirm_password    = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=2, max=50), EqualTo('password')])
    submit              = SubmitField('Register') 

    def validate_username(self, username):
        usersname_in_form = User_accnt.query.filter(User_accnt.username == username.data).first()
        if usersname_in_form:
            raise ValidationError('Username "'+username.data+'" is already taken. Please choose another')
    
    def validate_email(self, email):
        email_in_form = User_accnt.query.filter(User_accnt.email == email.data).first()
        if email_in_form:
            raise ValidationError('Email "'+email.data+'" is already taken. Please choose another')



# LOGIN PAGE
class LoginForm(FlaskForm):
    email       = StringField('Email', validators=[DataRequired(), Email()])
    password    = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=50)])
    remember    = BooleanField('Remember Me')
    submit      = SubmitField('Login')


