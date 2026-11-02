from flask_restful import Resource 
from flask import session,request,make_response
from app.models import Recipe 
from app.db import db

class RecipeIndex(Resource):
    def get(self):

        if session.get("user_id"):
            recipes=[recipe.to_dict(rules=("-user.password","-user.recipes",)) for recipe in Recipe.query.all()]

            return make_response(recipes,200)
            
        return {"message":"Unauthorized"},401

    def post(self):
        if session.get("user_id"):
            data=request.get_json()
            title=data.get("title")
            instructions=data["instructions"]
            minutes_to_complete=data.get("minutes_to_complete")

            if title and instructions and minutes_to_complete:
                recipe=Recipe(
                    title=title,
                    instructions=instructions,
                    minutes_to_complete=minutes_to_complete,
                    user_id=session["user_id"]

                )
                db.session.add(recipe)
                db.session.commit()

                response=recipe.to_dict(rules=("-user.password","-user.recipes"))

                return make_response(response,201)
            
            return {"message":"Fill all the fields"},422
        return {"message":"Unauthorized"},401

