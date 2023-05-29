import os
from urllib.parse import quote as url_quote

class Config:
    # Set up secret key
    SECRET_KEY = 'secret_key'
    FLASK_ENV = 'production'


    # SQLALCHEMY CONFIGS
    # SQLALCHEMY_DATABASE_URI = "mysql://nomad:{}@localhost/flaskapp?charset=utf8mb4".format(url_quote('qwe123!@#'))
    # SQLALCHEMY_DATABASE_URI = "mysql://nomad:{}@localhost/flaskapp".format(url_quote('qwe123!@#'))
    # SQLALCHEMY_BINDS = {
    #     'vetting': "mysql://nomad:{}@localhost/vetting?charset=utf8mb4".format(url_quote('qwe123!@#')),
    #     'db_test': 
    # }
    # SQLALCHEMY_TRACK_MODIFICATIONS = False



    