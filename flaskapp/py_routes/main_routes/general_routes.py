import os
from flask import render_template, jsonify, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

from flaskapp.py_routes.main_routes import main

# Models
from flaskapp.models.crud_model import job_application

# Forms
from flaskapp.py_forms.crud_forms import input_forms_job

from flaskapp import db, run_dammit
app = run_dammit()



# LANDING PAGE
# ===================================================================
@main.route('/', methods=['GET', 'POST'])
@main.route('/dashboard', methods=['GET', 'POST'])
def main_dashboard():
    page_title = 'Main page'

    if request.method == 'GET':
        return render_template('general/dashboard.html', page_title=page_title)
    


# Job application page
# ===================================================================
@main.route('/job_form', methods=['GET', 'POST'])
def job_form():
    page_title = 'Application page'
    form = input_forms_job()

    # if request.method == 'GET':
    if request.method == 'POST':
        # print('\n')
        # print('POST')
        # print('\n')
        if form.validate_on_submit:
            # print('validate on submit')
            first_name      = form.first_name.data
            print('first name: '+(str(first_name)))
            mid_name        = form.mid_name.data
            last_name       = form.last_name.data
            datepicker      = form.datepicker.data
            street_add      = form.street_add.data
            street_add_two  = form.street_add_two.data
            city            = form.city.data
            province        = form.province.data
            zip_code        = form.zip_code.data
            email           = form.email.data
            phone_num       = form.phone_num.data
            linkedin        = form.linkedin.data
            file_input      = form.file_input.data

            # Upload the resume to the folder
            sec_file        = secure_filename(file_input.filename)
            file_input.save(os.path.join(app.config['UPLOAD_FOLDER'], sec_file))
           
            # Renamed the file once save in folder
            renamed_resume_filepath = app.config['UPLOAD_FOLDER']+'/'+'RESUME_'+str(first_name)+'_'+str(last_name)+'_'+sec_file
            renamed_resume_name = 'RESUME_'+str(first_name)+'_'+str(last_name)+'_'+sec_file
            os.rename(app.config['UPLOAD_FOLDER']+'/'+sec_file, renamed_resume_filepath)

            save_dem_resume  = job_application(
                first_nm     = first_name,
                mid_nm       = mid_name,
                last_nm      = last_name,
                dob          = datepicker,
                add_st       = street_add,
                add_st_two   = street_add_two,
                add_city     = city,
                add_prov     = province,
                add_zip      = zip_code,
                email        = email,
                phn_num      = phone_num,
                linkedin     = linkedin,
                resume_file  = renamed_resume_name,
            )
            db.session.add(save_dem_resume)
            db.session.commit()

            flash('Application sent.', 'success')
            # return jsonify('done')

            return redirect(request.url)

    return render_template('general/job_form.html', page_title=page_title , form=form)

    




