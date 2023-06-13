import os, json
from urllib.parse import quote as url_quote

with open('/etc/valkur_configs.json') as config_file:
    config = json.load(config_file)


class Config:
    db_user = str(config.get("DBUSER"))
    db_pass = str(config.get("DBPASS"))
    
    SECRET_KEY = config.get("SK")
    FLASK_ENV = 'production'


    # SQLALCHEMY CONFIGS
    SQLALCHEMY_DATABASE_URI = config.get('DB_URI')
    # SQLALCHEMY_BINDS = {
    #     'db1': "mysql://user:{}@localhost/vetting?charset=utf8mb4".format(url_quote('pass')),
    #     'db2': 
    # }
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Upload the files from thje form
    UPLOAD_FOLDER = os.getcwd()+'/flaskapp/static/file_upload'
    ALLOWED_EXTENSIONS = {'doc', 'docx', 'pdf'}

    # EMAIL CONFIGS
    MAIL_SERVER     = str(config.get("MAIL_SERVER"))     
    MAIL_PORT       = str(config.get("MAIL_PORT"))
    MAIL_USERNAME   = str(config.get("MAIL_USERNAME"))
    MAIL_PASSWORD   = str(config.get("MAIL_PASSWORD"))
    MAIL_USE_TLS    = True
    MAIL_USE_SSL    = False
    send_email_to   = str(config.get("send_email_to"))

    