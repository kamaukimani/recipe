from flask_restful import Api 
from flask import Flask  
from .config import Config 
from .db import db,migrate,bcrypt 
from .models import *
from flask_restful import Api 
from .routes import *

def create_app():

    app=Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app) 
    migrate.init_app(app,db)
    bcrypt.init_app(app)
    api=Api(app)

    api.add_resource(Signup,'/signup',endpoint="signup")

    return app