from sqlalchemy.orm import Mapped,mapped_column,relationship  
from typing import List 
from sqlalchemy_serializer import SerializerMixin 
from app.db import db 
from sqlalchemy import ForeignKey 

class Recipe(db.Model,SerializerMixin):
    __tablename__= "recipes"

    serialize_rules=("-user.articles",)

    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]
    instructions:Mapped[str]
    minutes_to_complete:Mapped[int]

    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"))

    user:Mapped["User"] = relationship(back_populates="recipes")


    def __repr__(self):
        return f"<Recipe  {self.id}  {self.title}>"