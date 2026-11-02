from flask_restful import Resource 
from flask import session,request,make_response
from app.models import User 
from flask_bcrypt import Bcrypt 
from app.db import db

bcrypt=Bcrypt()

class Signup(Resource):
    def post(self):
        data=request.get_json()
        username=data["username"]
        password=data.get("password")
        image_url=data["image_url"]
        bio=data.get("bio")
        password_confirmation=data["password_confirmation"]

        if password != password_confirmation:
            return {"message":"Passwords do not match"},401

        exists=User.query.filter(User.username == username).first()

        if username and password and image_url and bio:
            if not exists:
                user=User(username=username,image_url=image_url,bio=bio)
                password_hash=bcrypt.generate_password_hash(password).decode("utf-8")
                user.password=password_hash

                db.session.add(user)
                db.session.commit()

                session["user_id"]=user.id 


                response=user.to_dict(rules=("-password",))
                return make_response(response,201)
            return {"message":"Username already exists"},401
        return {"message":"Provide data for all fields"},422
