from flask_restful import Api 
from flask import Flask  
from .config import Config 
from .db import db,migrate,bcrypt 
from .models import *
from flask_restful import Api 
from .routes import *
from flask_cors import CORS

def create_app():

    app=Flask(__name__)

    app.config.from_object(Config)
    CORS(app,origins=["http://localhost:3000","http://127.0.0.1:3000"],supports_credentials=True)

    db.init_app(app) 
    migrate.init_app(app,db)
    bcrypt.init_app(app)
    api=Api(app)

    api.add_resource(Signup,'/signup',endpoint="signup")
    api.add_resource(Login,'/login',endpoint='login')
    api.add_resource(CheckSession,'/check_session',endpoint="check_session")
    api.add_resource(Logout,'/logout',endpoint="logout")
    api.add_resource(RecipeIndex,'/recipes',endpoint="recipes")

    @app.before_request
    def check_if_logged_in():
        open_access_list=['signup','login','check_session']

        if (request.endpoint) not in open_access_list and (not session.get("user_id")):

            return {"message":"Unauthorized"},401


    return app