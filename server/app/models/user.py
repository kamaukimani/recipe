from sqlalchemy.orm import Mapped,mapped_column,relationship  
from typing import List 
from sqlalchemy_serializer import SerializerMixin 
from app.db import db 

class User(db.Model,SerializerMixin):
    __tablename__="users"

    serialize_rules=("-recipes.user",)
    
    id:Mapped[int]=mapped_column(primary_key=True)
    username:Mapped[str]=mapped_column(unique=True)
    password:Mapped[str]
    image_url:Mapped[str]
    bio:Mapped[str]

    recipes:Mapped[List["Recipe"]]=relationship(back_populates="user",cascade="all,delete-orphan")

    def __repr__(self):
        return f"<User {self.id}  {self.username}>"