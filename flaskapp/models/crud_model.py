from datetime import datetime
from flaskapp import db
from sqlalchemy.sql import func

class job_application(db.Model):
    __tablename__    = 'job_app'
    __table_args__   = {'mysql_charset':'utf8mb4'}
    id            = db.Column(db.Integer, primary_key=True)
    first_nm      = db.Column(db.String(100))
    mid_nm        = db.Column(db.String(100))
    last_nm	      = db.Column(db.String(100))
    dob           = db.Column(db.String(10))

    add_st      = db.Column(db.String(255))
    add_st_two  = db.Column(db.String(255))
    add_city    = db.Column(db.String(100))
    add_prov    = db.Column(db.String(100))
    add_zip     = db.Column(db.String(100))

    email       = db.Column(db.String(20))
    phn_num     = db.Column(db.String(20))
    linkedin    = db.Column(db.String(100))

    resume_file = db.Column(db.String(100))
    
    dt_created  = db.Column(db.DateTime(timezone=True), server_default=func.now())


    def to_dict(self):
        return{
            'id'            : self.id,
            'first_nm'      : self.first_nm,
            'mid_nm'        : self.mid_nm,
            'last_nm'       : self.last_nm,
            'dob'           : self.dob,
            'add_st'        : self.add_st,
            'add_st_two'    : self.add_st_two,
            'add_city'      : self.add_city,
            'add_prov'      : self.add_prov,
            'add_zip'       : self.add_zip,
            'email'         : self.email,
            'phn_num'       : self.phn_num,
            'linkedin'      : self.linkedin,
            'resume_file'   : self.resume_file,
            'dt_created'    : self.dt_created,
        }


 
