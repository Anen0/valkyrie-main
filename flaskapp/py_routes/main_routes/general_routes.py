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
    # form = Basic_post()

    if request.method == 'GET':
        return render_template('general/dashboard.html', page_title=page_title)

    # if request.method == 'POST':
    #     st_str = request.form['s_string']
    #     st_int = request.form['s_int']
    #     st_txt = request.form['s_txt']

    #     form_data = Crud_tbl(
    #         some_string   = st_str,
    #         some_int      = st_int,
    #         some_text     = st_txt
    #     )
    #     db.session.add(form_data)
    #     db.session.commit()

    #     status = jsonify({
    #             'string': st_str,
    #             'integer': st_int,
    #             'text': st_txt,
    #             'status':'ADDED'
    #         })
    #     return status
    



@main.route('/crud_view', methods=['GET'])
def crud_view():
    if request.method == 'GET':
        views = Crud_tbl.query.all()
        tmp_list = list()
        for i in views:
            k = {
                'ct_id'        : i.ct_id,
                'some_string'  : i.some_string,
                'some_text'    : i.some_text,
                'some_int'     : i.some_int,
                'dtg'     : i.dtg
            }
            tmp_list.append(k)
        # return jsonify(tmp)

            tmp = table_builder.crud_dt_serverside(request, tmp_list)
        return jsonify(tmp)
        


@main.route('/crud_update', methods=['GET', 'POST'])
def crud_update():
    pass

@main.route('/crud_delete', methods=['GET', 'POST'])
def crud_delete():
    pass



@main.route('/dashboard_h', methods=['GET', 'POST'])
def main_dashboard_h():
    page_title = 'Main page - Horizontal'

    if request.method == 'GET':
        return render_template('general/dashboard_H.html', page_title=page_title)



# CRUD page
# ===================================================================





