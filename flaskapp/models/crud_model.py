from datetime import datetime
from flaskapp import db
from sqlalchemy.sql import func

class Crud_tbl(db.Model):
    __tablename__    = 'crud_tbl'
    __table_args__   = {'mysql_charset':'utf8mb4'}
    ct_id            = db.Column(db.Integer, primary_key=True)
    some_string      = db.Column(db.String(20))
    some_text        = db.Column(db.Text)
    some_int	     = db.Column(db.Integer)
    # dtg              = db.Column(db.DateTime)
    dtg              = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def to_dict(self):
        return{
            'ct_id'       : self.ct_id,
            'some_string' : self.some_string,
            'some_text'   : self.some_text,
            'some_int'    : self.some_int,
            'dtg'         : self.dtg
        }

    # def __repr__(self):
    #     return f"Crud_tbl('{self.ct_id}', '{self.some_string}', '{self.some_text}', '{self.some_int}')"

    # def __init__(self, ct_id, some_string, some_text, some_int):
    #     self.ct_id = ct_id
    #     self.some_string = some_string
    #     self.some_text = some_text
    #     self.some_int = some_int

 
