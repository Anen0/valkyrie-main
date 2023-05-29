#!/usr/bin/env python
# PACKAGES
from flask import Flask
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jsglue import JSGlue
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager

# Call config
from flaskapp.config import Config


# SET PACKAGES
# mysql           = MySQL()
db              = SQLAlchemy()
migrate         = Migrate()
bcrypt          = Bcrypt()
login_manager   = LoginManager()
jsglue          = JSGlue() # enables url_for to be used on the front-end


# APPLICATION PROPER
def run_dammit(config_class=Config):
    app = Flask(__name__)

    # Initialize config file
    app.config.from_object(Config)


    # Initialize packages
    # mysql.init_app(app)
    # db.init_app(app)
    migrate.init_app(app, db)
    # bcrypt.init_app(app)
    jsglue.init_app(app)

    
    # login_manager.init_app(app)
    # login_manager.login_view = 'main.login'
    # login_manager.login_message_category = 'info'
    

    from flaskapp.py_routes.main_routes.general_routes import main

    app.register_blueprint(main)

    # with app.test_request_context():
    #     db.create_all()
    

    return app
