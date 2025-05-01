from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Recipe(Base):
    __tablename__= "recipes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    time = Column(Integer)
    category = Column(String)
    image = Column(String)
    isFavorite = Column(Boolean, default=False)