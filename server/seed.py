
from random import randint, choice as rc

from faker import Faker

from app import create_app
from app.db import db
from app.models import Recipe, User
from flask_bcrypt import Bcrypt


bcrypt=Bcrypt()
fake = Faker()

app=create_app()

with app.app_context():

    Recipe.query.delete()
    #User.query.delete()

    fake = Faker()


    # make sure users have unique usernames
    print("Adding users......")
    users = []
    usernames = []

    for i in range(20):
        
        username = fake.first_name()
        while username in usernames:
            username = fake.first_name()
        usernames.append(username)


        username=username
        password=fake.password()
        bio=fake.paragraph(nb_sentences=3)
        image_url=fake.url()

        password_hash=bcrypt.generate_password_hash(password).decode("utf-8")

        user=User(username=username,password=password_hash,bio=bio,image_url=image_url,)

        

        users.append(user)

    db.session.add_all(users)

    print("Adding recipes.....")

    recipes = []

    for user in users:
        for i in range(randint(1,5)):
            instructions = fake.paragraph(nb_sentences=8)

            recipe=Recipe(
                title=fake.sentence(),
                instructions=instructions,
                minutes_to_complete=randint(15,90),
                user=user,
            )
            recipes.append(recipe)
        db.session.add_all(recipes)
        db.session.commit()
    

print("Complete!!")