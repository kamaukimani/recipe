from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from flask_bcrypt import Bcrypt 
from sqlalchemy.orm import DeclarativeBase  

class Base(DeclarativeBase):
    pass 

db=SQLAlchemy(model_class=Base)
migrate=Migrate()
bcrypt=Bcrypt()