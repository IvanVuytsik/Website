from flask import Flask, session, Blueprint, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path
import json

db = SQLAlchemy()           #database
DB_NAME = 'database.db'     #database

def create_app():
    app = Flask(__name__)
    app.config["SERET_KEY"] = 'filesystem'
    app.secret_key = 'super secret key'
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}' #database
    db.init_app(app)  #database
    #engine = create_engine(f'sqlite:///{DB_NAME}')



    from views import views
    from auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #from .models import User, Note     #database
    from models import User, Note
    from models import Note 

    create_database(app)    #database

    #-------------------login manager------------------------
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user (id):
        return User.query.get(int(id))
    #-------------------login manager^------------------------

    return app

#database
def create_database(app):
    if not path.exists('venv/' + DB_NAME): #check if database exists
        db.create_all(app=app) #which app we are creating a database for)
        print('Created Database!')





