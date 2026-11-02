from flask_restful import Resource 
from flask import session,request,make_response
from app.models import Recipe 
from app.db import db

class RecipeIndex(Resource):
    def get(self):

        if session.get("user_id"):
            recipes=[recipe.to_dict() for recipe in Recipe.query.all()]

            return make_response(recipes,200)
            
        return {"message":"Unauthorized"},401