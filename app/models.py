from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.dialects.sqlite import JSON  # Use JSON for SQLite
from .database import Base

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    time = Column(Integer)
    category = Column(String)
    image = Column(String)
    isFavorite = Column(Boolean, default=False)
    ingredients = Column(JSON, nullable=True)  # Store ingredients as JSON
    directions = Column(JSON, nullable=True)  # Store directions as JSON
    nutritionInfo = Column(JSON, nullable=True)  # Store nutrition info as JSON