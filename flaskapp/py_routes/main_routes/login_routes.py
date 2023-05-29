import os, secrets
from PIL import Image
from flask import render_template, jsonify, request, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required

# Models
from flaskapp.models.accounts_model import User_accnt

# Forms
from flaskapp.py_forms.accounts_forms import RegisterForm, LoginForm

from flaskapp import db, bcrypt, run_dammit

from . import main


# REGISTRATION PAGE-------------------------------------------------------------------------------------------------
@main.route('/register', methods=['GET', 'POST'])
def register():
    page_data = 'Register page'
    form = RegisterForm()

    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user_data = User_accnt(
                username    = form.username.data,
                email       = form.email.data,
                accnt_type  = 'regular',
                status      = 'active',
                password    = hashed_password
            )
            db.session.add(user_data)
            db.session.commit()
            flash(f'Account created for {form.username.data}!', 'primary')

            return redirect(url_for('main.login'))

    return render_template('login_pages/register.html', page_data=page_data, form=form)



# LOGIN PAGE----------------------------------------------------------------------------------------------------------
@main.route('/login', methods=['GET', 'POST'])
def login():
    page_data = 'Login page'
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        if form.validate_on_submit():
            user_data = User_accnt.query.filter_by(email=form.email.data).first()
            if user_data and bcrypt.check_password_hash(user_data.password, form.password.data):
                # this is where the user is logged in
                login_user(user_data, remember = form.remember.data)

                flash(f'Welcome, logged in as {user_data.username}!', 'success')
                
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('main.main_dashboard'))
            else:
                flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('login_pages/login.html', page_data=page_data, form=form)


# LOGOUT------------------------------------------------------------------------------------------------------------
@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.login'))




