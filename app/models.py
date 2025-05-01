from sqlalchemy import Column, Integer, String
from .database import Base

class Recipe(Base):
    __tablename__= "recipes"
    id = Column(int, primary_key=True, index=True)
    title = Column(str, index=True)
    time = Column(int)
    type = Column(str)
    image = Column(str)
    isFavourite = Column(bool)