import os, json
from urllib.parse import quote as url_quote

with open('/etc/valkur_configs.json') as config_file:
    config = json.load(config_file)


class Config:
    # db_user = str(config.get("DBUSER"))
    # db_pass = str(config.get("DBPASS"))
    # Set up secret key
    SECRET_KEY = 'config.get("SK")'
    FLASK_ENV = 'production'


    # SQLALCHEMY CONFIGS
    # SQLALCHEMY_DATABASE_URI = str(config.get('SQLALCHEMY_DATABASE_URI'))
    SQLALCHEMY_DATABASE_URI = "mysql://nomad:{}@localhost/val-tbl".format(url_quote('qwe123xU'))
    # SQLALCHEMY_BINDS = {
    #     'vetting': "mysql://nomad:{}@localhost/vetting?charset=utf8mb4".format(url_quote('qwe123!@#')),
    #     'db_test': 
    # }
    SQLALCHEMY_TRACK_MODIFICATIONS = False



    