from flask import render_template, jsonify, request, redirect, url_for, flash
# from flask_login import login_user, current_user, logout_user, login_required

# Models
from flaskapp.models.accounts_model import User_accnt
from flaskapp.models.crud_model import Crud_tbl

# Forms
# from flaskapp.py_forms.crud_forms import Basic_post

from flaskapp import db

from flaskapp.py_routes.main_routes import main


# LANDING PAGE
# ===================================================================
@main.route('/', methods=['GET', 'POST'])
@main.route('/dashboard', methods=['GET', 'POST'])
# @login_required
def main_dashboard():
    page_title = 'Main page'

    if request.method == 'GET':
        return render_template('general/dashboard.html', page_title=page_title)
    

@main.route('/app_form', methods=['GET', 'POST'])
def app_form():
    page_title = 'Application page'

    if request.method == 'GET':
        return render_template('general/job_form.html', page_title=page_title)



# CRUD page
# ===================================================================





