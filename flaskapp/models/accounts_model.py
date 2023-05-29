from datetime import datetime
from flaskapp import db, login_manager
from flask_login import UserMixin


# USER MODEL---------------------------------------------------------------------------------------------
# @login_manager.user_loader
# def load_user(user_id):
#     return User_accnt.query.get(int(user_id))

class User_accnt(db.Model, UserMixin):
    __tablename__    = 'user_accnt'
    __table_args__   = {'mysql_charset':'utf8mb4'}
    user_id          = db.Column(db.Integer, primary_key=True)
    username         = db.Column(db.String(100), unique=True, nullable=False)
    email            = db.Column(db.String(100), unique=True, nullable=False)
    prof_pic         = db.Column(db.String(200), nullable=False, default='user.png')
    accnt_type	     = db.Column(db.String(20))
    status           = db.Column(db.String(20))
    password         = db.Column(db.String(255), nullable=False)

    # needs this line for user_login to work
    def get_id(self):
        return self.user_id

    def to_dict(self):
        return{
            'user_id'   : self.user_id,
            'username'  : self.username,
            'email'     : self.email,
            'prof_pic'  : self.prof_pic,
            'accnt_type': self.accnt_type,
            'status'    : self.status,
            'password'  : self.password
        }


