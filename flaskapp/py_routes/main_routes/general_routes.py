import os
from datetime import datetime
from flask import render_template, jsonify, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

from flaskapp.py_routes.main_routes import main

# Models
from flaskapp.models.crud_model import job_application

# Forms
from flaskapp.py_forms.crud_forms import input_forms_job

from flaskapp import db, mail, run_dammit
from flask_mail import Message
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
        if form.validate_on_submit:
            first_name      = form.first_name.data
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

            cur = datetime.now()
            display_dt = str(cur.month)+'-'+str(cur.day)+'-'+str(cur.year)+'_'+str(cur.hour)+':'+str(cur.minute)+':'+str(cur.second)
            display_wrd = str(cur.strftime('%B'))+' '+str(cur.strftime('%d'))+', '+str(cur.strftime('%Y'))+' '+str(cur.hour)+':'+str(cur.minute)+':'+str(cur.second)

            # Upload the resume to the folder
            sec_file = secure_filename(file_input.filename)
            file_input.save(os.path.join(app.config['UPLOAD_FOLDER'], sec_file))

           
            # Renamed the file once save in folder +'_'+str(display_dt)
            renamed_resume_name     = 'RESUME_'+str(first_name)+'_'+str(last_name)+'_'+display_dt+'_'+sec_file
            renamed_resume_filepath = app.config['UPLOAD_FOLDER']+'/'+renamed_resume_name
            os.rename(app.config['UPLOAD_FOLDER']+'/'+sec_file, renamed_resume_filepath)

            # print('\n')
            # print('\n')
            # print('renamed_resume_name')
            # print(renamed_resume_name)
            # print('\n')
            # print('renamed_resume_filepath')
            # print(renamed_resume_filepath)
            # print('\n')
            # print('\n')


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

            body = ''
            if linkedin:
                body = f'''Recieved job application from {str(first_name)} {str(mid_name)} {str(last_name)}.\n  
Sent on {str(display_wrd)}. \n 
Contact details: 
Email: {str(email)} 
Phone: {str(phone_num)}
LinkedIn link: {str(linkedin)}'''
            else:
                body = f'''Recieved job application from {str(first_name)} {str(mid_name)} {str(last_name)}.\n  
Sent on {str(display_wrd)}.\n 
Contact details: \n 
Email: {str(email)}
Phone: {str(phone_num)}'''
            
            subject = 'VALKYRIE APPLICANT RESUME: '+str(first_name)+' '+str(last_name)
            
            # print('\n')
            # print('\n')
            # print(body)
            # print('\n')
            # print('\n')
            # print(subject)
            # print('\n')

            msg = Message(subject = subject, 
                          sender = app.config['MAIL_USERNAME'], 
                          recipients = ["valkyrie@ashgard.com.ph"],
                          body = body,
                        )
            # recipients= ["valkyrie@ashgard.com.ph"],
            msg.add_recipient("wW1nd0waker@gmail.com")
            src = str(app.config['UPLOAD_FOLDER']+'/'+renamed_resume_name)
            with app.open_resource(src) as fp:
                msg.attach(renamed_resume_name, "application/pdf", fp.read())
            
                mail.send(msg)



            flash('Application has been sent. A resonse will be sent to your email .', 'success')
            return redirect(request.url)


    return render_template('general/job_form.html', page_title=page_title , form=form)

    




