from pydantic import BaseModel
from typing import Optional, Union, List
from fastapi import UploadFile

class Recipe(BaseModel):
    id: Optional[int] = None
    name: str
    time: int
    category: str
    image: Optional[Union[str, UploadFile]] = None  # Accept file uploads or URLs
    isFavorite: Optional[bool] = None
    ingredients: Optional[List[str]] = None  # List of ingredients
    directions: Optional[List[str]] = None  # List of directions
    nutritionInfo: Optional[List[dict]] = None  # List of nutrition info (name and measure)
